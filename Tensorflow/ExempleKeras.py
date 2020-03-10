#######################################
#Paquests
#######################################
#Aquí tots els paquets que farem servir 
from __future__ import print_function
from keras.callbacks import LambdaCallback
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np
import random
import sys
import io

'''Anomenem path al fitxer nietzsche.txt que està ubicat al url donat.'''
path = get_file(
    'nietzsche.txt',
    origin='https://s3.amazonaws.com/text-datasets/nietzsche.txt') 

'''Obrim el fitxer path amb codificació utf-8 com a f, llegim f en minuscules i donem la longitud del cos del text'''
with io.open(path, encoding='utf-8') as f:
    text = f.read().lower() #lower() passa a minusculas
print('corpus length:', len(text))

'''Definim com a chars la llista ordenada de caracters que apareixen en el text. Després imprimim la longitut de tots els caracters que hem llegit'''
chars = sorted(list(set(text))) #sorted() Ordena
print('total chars:', len(chars))
'''He fet un exemple, com estàn ordenats realment és com que tenim els dos diccionaris per traduir de un al altre print(indices_char,char_indices)
{0: 'eyes', 1: 'hola', 2: 'make', 3: 'rip'}, {'eyes': 0, 'rip': 3, 'make': 2, 'hola': 1}'''
char_indices = dict((c, i) for i, c in enumerate(chars)) #enumerate() enumera els elements de una llista 
#dict() metode per crear un diccionari
indices_char = dict((i, c) for i, c in enumerate(chars))

# cut the text in semi-redundant sequences of maxlen characters
'''Aquí la idea es tallar el text en secuencies semi-redudants de caracters amb mida maxlen'''
maxlen = 40 #mida maxima
step = 3 #
sentences = [] # Llista buida amb frases
next_chars = [] # Llista amb el seguent caracter 
''' Per i de 0 fins a  la llargada del text menys maxlen de step en step (de tres en tres) afeggim a la llista '''
for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])
print('nb sequences:', len(sentences))

print('Vectorization...')
x = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        x[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1


# build the model: a single LSTM
print('Build model...')
model = Sequential()
model.add(LSTM(128, input_shape=(maxlen, len(chars))))
model.add(Dense(len(chars), activation='softmax'))

optimizer = RMSprop(learning_rate=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)


def sample(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)


def on_epoch_end(epoch, _):
    # Function invoked at end of each epoch. Prints generated text.
    print()
    print('----- Generating text after Epoch: %d' % epoch)

    start_index = random.randint(0, len(text) - maxlen - 1)
    for diversity in [0.2, 0.5, 1.0, 1.2]:
        print('----- diversity:', diversity)

        generated = ''
        sentence = text[start_index: start_index + maxlen]
        generated += sentence
        print('----- Generating with seed: "' + sentence + '"')
        sys.stdout.write(generated)

        for i in range(400):
            x_pred = np.zeros((1, maxlen, len(chars)))
            for t, char in enumerate(sentence):
                x_pred[0, t, char_indices[char]] = 1.

            preds = model.predict(x_pred, verbose=0)[0]
            next_index = sample(preds, diversity)
            next_char = indices_char[next_index]

            sentence = sentence[1:] + next_char

            sys.stdout.write(next_char)
            sys.stdout.flush()
        print()

print_callback = LambdaCallback(on_epoch_end=on_epoch_end)

model.fit(x, y,
          batch_size=128,
          epochs=60,
          callbacks=[print_callback]) 
