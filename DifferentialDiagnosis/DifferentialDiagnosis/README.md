# Differential Diagnosis - Part I

![](RackMultipart20210429-4-12d94nh_html_237499165a11f2b9.gif)

## Overview

Part 1 of the project involves classifying input images into top &#39;k&#39; most probable lesion types.

Input: Lesion image

Output: &#39;k&#39; nearest images

## Requirements

opencv-python==4.5.1.48

tensorflow==2.4.1

google-cloud-storage==1.37.1

numpy==1.19.5

## Command to run code

| python main.py |
| --- |

## Functions

### **Download file function**

| **download\_file(bucket\_name, file\_name, output\_fname)** |
| --- |

**Description:**

Function to download a file from google cloud storage.

**Parameters:**

bucket\_name : str (Name of bucket in google cloud storage)

file\_name : str (Name of file to download)

output\_fname : str (Name of output file)

### **Download bytes function**

| **download\_bytes(bucket\_name, file\_name)** |
| --- |

**Description:**

Function to download file in bytes from google cloud storage.

**Parameters:**

bucket\_name : str (Name of bucket in google cloud storage)

file\_name : str (Name of file to download)

**Returns:**

Base64 encoded string.

### **Load model function**

| **load\_model(bucket\_name, file\_name, output\_fname)** |
| --- |

**Description:**

Function to load model from cloud storage.

**Parameters:**

bucket\_name : str (Name of bucket in google cloud storage)

file\_name : str (Name of file to download)

output\_fname : str (Name of output file)

**Returns:**

Model.

### **Load image function**

| **load\_image(img\_bytes, shape=None, color\_format=&#39;rgb&#39;)** |
| --- |

**Description:**

Function to convert image in bytes to numpy array.

**Parameters:**

img\_bytes : bytes

shape : tuple or list

color\_format : str

**Returns:**

Image as a numpy array.

### **Preprocess function**

| **preprocess(img)** |
| --- |

**Description:**

Function to standardize the pixels values using z-score.

**Parameters:**

img : Image

**Returns:**

Standardized image.

### **Make prediction function**

| **make\_prediction(inp, model, top\_k=3)** |
| --- |

**Description:**

Function to predict the lesion type.

**Parameters:**

inp : numpy array

model : tensorflow model

top\_k : int

**Returns:**

A list of tuples, &#39;top\_k&#39; results along with probabilities.