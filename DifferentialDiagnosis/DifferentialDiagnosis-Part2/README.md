# Differential Diagnosis - Part II

![](RackMultipart20210429-4-104f8oe_html_237499165a11f2b9.gif)

## Overview

Part 2 of the project involves obtaining the differential diagnosis from the inputs given.

Inputs: Values of type of lesion (obtained from part 1), number of lesions, body location, age, gender, itching, fever, rate of development, appearance of patient.

Output: Images and description of the diagnosis results.

## Requirements

google-cloud-storage==1.37.1

numpy==1.19.5

pandas==1.2.4

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

### **Load metadata function**

| **load\_metadata(bucket\_name, file\_name, output\_fname=****&#39;/tmp/metadata.csv&#39;****)** |
| --- |

**Description:**

Function to download metadata from google cloud storage.

**Parameters:**

bucket\_name : str (Name of bucket in google cloud storage)

file\_name : str (Name of file to download)

output\_fname : str (path to temporary file)

**Returns:**

Metadata as a 2-D numpy array.

### **Convert age to age band function**

| **convert\_age\_to\_age\_band(age, age\_mapping)** |
| --- |

**Description:**

Maps age into 1 of 8 unique values.

**Parameters:**

age : int

age\_mapping : dict

**Returns:**

Mapped age (int).

### **Predict disease function**

| **predict\_disease(metadata, type\_of\_lesion, no\_of\_lesions, body\_location,****age, gender, itching, fever, rate\_of\_dev, appearance)** |
| --- |

**Description:**

Function to predict the disease.

**Parameters:**

metadata : numpy array (Metadata on all diseases)

type\_of\_lesion : str

no\_of\_lesions : str (solitary | multiple)

body\_location : str

age : int

gender : str (Male | Female)

itching : str (Yes | No | Sometimes)

fever : str (Yes | No)

rate\_of\_dev : str

appearance : str

**Returns:**

Most probable diseases along with description.