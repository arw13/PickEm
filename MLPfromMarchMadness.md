# MLP model
MLP = Sequential()
MLP.name = 'MLP'
MLP.add(Dense(5, input_dim=xDim, kernel_initializer='glorot_normal',activation = 'tanh'))
MLP.add(Dropout(dropRate))
MLP.add(Dense(200,kernel_initializer='glorot_normal',activation = 'tanh'))
MLP.add(Dropout(dropRate))
MLP.add(Dense(200, kernel_initializer='glorot_normal',activation = 'tanh'))
MLP.add(Dropout(dropRate))
MLP.add(Dense(1, kernel_initializer='glorot_normal', activation='sigmoid'))

# Compile model
adam = optimizers.Adam(lr=learningRate, amsgrad=True)
MLP.compile(loss='binary_crossentropy', optimizer=adam, metrics=['accuracy'])