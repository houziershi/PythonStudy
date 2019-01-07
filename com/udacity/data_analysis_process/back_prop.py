import numpy as np


def sigmoid(x):
    """
    Calculate sigmoid
    """
    return 1 / (1 + np.exp(-x))


def sigmoid_prim(x):
    """
    Calculate derivative of sigmoid
    :param x:
    :return:
    """
    return sigmoid(x) * (1 - sigmoid(x))

x = np.array([0.5, 0.1, -0.2])
print(x)
print(x[:, None].shape)
target = 0.6
learnrate = 0.5

weights_input_hidden = np.array([[0.5, -0.6],
                                 [0.1, -0.2],
                                 [0.1, 0.7]])
print(weights_input_hidden[:, None],'======',weights_input_hidden[:, None].shape)
print(np.reshape(weights_input_hidden,(2,3)))
weights_hidden_output = np.array([0.1, -0.3])

## Forward pass
hidden_layer_input = np.dot(x, weights_input_hidden)
hidden_layer_output = sigmoid(hidden_layer_input)

output_layer_in = np.dot(hidden_layer_output, weights_hidden_output)
output = sigmoid(output_layer_in)

## Backwards pass
## TODO: Calculate output error
error = target - output

# TODO: Calculate error term for output layer
output_error_term = error * output * (1 - output)
print('output_error_term ======', output_error_term)

# TODO: Calculate error term for hidden layer
hidden_error_term = weights_hidden_output*output_error_term* hidden_layer_output * (1 - hidden_layer_output)
print('hidden_error_term =======', hidden_error_term)

# TODO: Calculate change in weights for hidden layer to output layer
delta_w_h_o = learnrate*output_error_term*hidden_layer_output

# TODO: Calculate change in weights for input layer to hidden layer
delta_w_i_h = learnrate*hidden_error_term*x[:, None]

print('Change in weights for hidden layer to output layer:')
print(delta_w_h_o)
print('Change in weights for input layer to hidden layer:')
print(delta_w_i_h)
