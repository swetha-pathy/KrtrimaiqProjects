# Differential Diagnosis - Model training

## ![](RackMultipart20210429-4-1pexlio_html_237499165a11f2b9.gif) Overview

Training for a neural network model to classify lesion types.

## Requirements

tensorflow==2.4.1

numpy==1.19.5

opencv-python==4.1.2

matplotlib==3.2.2

scikit-learn==0.22.2.post1

## Functions

### **Load image function:**

| **load\_img(path, shape)** |
| --- |

**Description:**

Function to load image

**Parameters:**

path : path-like (path to images)

shape : tuple or list

**Returns:**

Image resized to the input shape.

### **Z-score standardization function:**

| **standardize(img)** |
| --- |

**Description:**

Function to standardize image using z-score.

**Parameters:**

img : Image

**Returns:**

Standardized image.

### **Uniform standardization function:**

| **uniform\_std(img)** |
| --- |

**Description:**

Function to perform uniform standardization (0-1) of images.

**Parameters:**

img : Image

**Returns:**

Standardized image.

### **Get generator function:**

| **get\_generator(path, batch\_size, classes, input\_shape=(256, 256))** |
| --- |

**Description:**

To create a python generator which yields batches of inputs for the model and true labels.

**Parameters:**

path : path-like (path to images)

batch\_size : int

classes : dict (class mapping)

input\_shape : tuplr or list

**Returns:**

Batches of inputs.

### **Create model function:**

| **create\_model(input\_shape, no\_classes)** |
| --- |

**Description:**

Function to create a tf model.

**Parameters:**

input\_shape : 3-D tuple (input shape of the model)

no\_classes : int (number of classes in output layer)

**Returns:**

Model.

### **Training function:**

| **training(model, train\_gen, epochs, steps\_per\_epoch, validation\_steps, filename=&#39;0&#39;)** |
| --- |

**Description:**

Trains the model and saves the checkpoint.

**Parameters:**

model : tf model

train\_gen : generator

epochs : int

steps\_per\_epoch : int

validation\_steps : int

filename : str (used to serialize checkpoint)

###