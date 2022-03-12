We used a bare inception model to train on the oxford flowers dataset. The dataset has 1020 training, 1020 validation and 6149 test examples.

<img src="https://user-images.githubusercontent.com/480644/134114129-488002ca-37cc-41c0-9df9-d3626da4de2f.png" width="50%">

It has 102 distinct flower labels. Each image is assigned a unique label.

We experimented with several data augmentation techniques. The results are described in the later sections. All the experiments are run with the following prameters unless otherwise stated:
* Base Model: Inception
* Epochs: 30
* Batch Size: 64
* PreOps: Normalization and Resize (180x180)
* Dataset: oxford_flowers102

## Attempt 1
Regular training without any modifications to the dataset.
<table>
  <thead>
    <tr>
      <th align="center" colspan="2">Training Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><img width="60%" src="https://user-images.githubusercontent.com/480644/134125333-cdeea1d4-bfd6-4790-9287-acf2174d4872.png"></td>
      <td align="center"><img width="60%" src="https://user-images.githubusercontent.com/480644/134125400-40f87081-73d2-4fde-bbf0-f8491cd35535.png"></td>
    </tr>
    <tr>
      <td colspan="2"><p align="center"><img width="80%" src="https://user-images.githubusercontent.com/480644/134125025-fe9617cf-3ab1-4fe7-9612-5ba95302205a.png"></p></td>
    </tr>
  </tbody>
</table>

## Attempt 2 [Pretrained Weights]
* Pretrained Imagenet Weights
* A dropout (0.33) layer prior to the softmax layer.
* Batch Size: 128
<table>
  <thead>
    <tr>
      <th align="center" colspan="2">Training Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><img width="60%" src="https://user-images.githubusercontent.com/480644/134286439-6dc30cf0-06e1-4ae9-bf07-7347130fa837.png"></td>
      <td align="center"><img width="60%" src="https://user-images.githubusercontent.com/480644/134286492-ef1e5ba3-6618-4465-b3f3-14ca8c378f9f.png"></td>
    </tr>
    <tr>
      <td align="center" colspan="2"><img width="80%" src="https://user-images.githubusercontent.com/480644/134286368-eff2f839-cf62-431c-b0a5-c97f5026a93f.png"></td>
    </tr>
  </tbody>
</table>

## Attempt 3 [Basic Augmentations]
* Pretrained Imagenet Weights
* A dropout (0.33) layer prior to the softmax layer.
* Training With Augmentations: RandomContrast(.7), RandomZoom(height_factor=(-.4, 0)
* Epochs: 100
* Batch Size: 128
<table>
  <thead>
    <tr>
      <th align="center" colspan="2">Training Summary</th>
    </tr>
  </thead>
  <tbody>
    <td align="center" colspan="2"><img width="80%" src="https://user-images.githubusercontent.com/480644/134291501-2e726cae-8529-4043-b041-433b0f3e2975.png"></td>
    <tr>
      <td align="center"><img width="60%" src="https://user-images.githubusercontent.com/480644/134291707-da960dd4-3f01-4323-b657-69fa05719873.png"></td>
      <td align="center"><img width="60%" src="https://user-images.githubusercontent.com/480644/134291785-26b1672d-e41c-4191-881c-79fcb4154772.png"></td>
    </tr>
    <tr>
      <td align="center" colspan="2"><img width="80%" src="https://user-images.githubusercontent.com/480644/134291600-c0fd7902-c860-49df-9dde-6f901725e919.png"></td>
    </tr>
  </tbody>
</table>

## Attempt 4 [RandAugment]
* Pretrained Imagenet Weights
* A dropout (0.33) layer prior to the softmax layer.
* RandAugment: N=3, M=9
* Batch Size: 128
<table>
  <thead>
    <tr>
      <th align="center" colspan="2">Training Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center" colspan="2"><img width="80%" src="https://user-images.githubusercontent.com/480644/134322539-5c08c45b-efd7-4ea7-962e-3c076354f057.png"></td>
    </tr>
    <tr>
      <td align="center"><img width="60%" src="https://user-images.githubusercontent.com/480644/134323136-4e510e97-b69e-47f1-a1b2-428dba603881.png"></td>
      <td align="center"><img width="60%" src="https://user-images.githubusercontent.com/480644/134323271-81393bfd-5f69-4778-9b6d-738995443efe.png"></td>
    </tr>
    <tr>
      <td align="center" colspan="2"><img width="80%" src="https://user-images.githubusercontent.com/480644/134323028-8e6dce27-8357-4dfb-804d-b827ab267ef3.png"></td>
    </tr>
  </tbody>
</table>

## Attempt 4 [With a Dense 124 Layer]
* Pretrained Imagenet Weights
* Inception=>Dropout(0.33)=>Dense(124)=>Dropout(0.33)=>Softmax()
* RandAugment: N=3, M=9
* Epochs: 30 + 70 + 50
* Batch Sizes: 128, 128, 64, 32 
<table>
  <thead>
    <tr>
      <th align="center" colspan="2">
        Training Summary
        <sub><a href="https://www.dropbox.com/sh/fvgbdks5qajhuyl/AAB94fe1XvmNFa_m1I0Pfc6va?dl=0">[link]</a></sub>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center" colspan="2"><img width="80%" src="https://user-images.githubusercontent.com/480644/134459907-0e48c10e-9687-4057-a317-96d57e19900e.png"></td>
    </tr>
    <tr>
      <td align="right">
        <img width="40%" src="https://user-images.githubusercontent.com/480644/134459971-40c0d977-610f-4db3-9f38-365b46da79d9.png">
        <img width="40%" src="https://user-images.githubusercontent.com/480644/134463287-fbfbbdbe-bc65-42b4-bd3e-069558f0fa87.png">
        <img width="40%" src="https://user-images.githubusercontent.com/480644/134466375-12d9ee37-457b-497b-8fa6-60243abace98.png">
      </td>
      <td align="left">
        <img width="40%" src="https://user-images.githubusercontent.com/480644/134460023-4177f38d-b04c-4c64-b9ca-c9c1ba4f922e.png">
        <img width="40%" src="https://user-images.githubusercontent.com/480644/134463486-bc0bb0d2-b7df-4cdb-a5a8-e782237c7315.png">
        <img width="40%" src="https://user-images.githubusercontent.com/480644/134466475-87c309b7-34bd-47b8-93bb-b020787dd7e3.png">
      </td>
    </tr>
    <tr>
      <td align="center" colspan="2">
        <img width="80%" src="https://user-images.githubusercontent.com/480644/134459833-4a4a2ae1-6d16-4355-9a52-63b969206690.png">
        <img width="80%" src="https://user-images.githubusercontent.com/480644/134464101-6e26d49a-91e6-4ba8-b8c7-3cec1aaf0f5d.png">
        <img width="80%" src="https://user-images.githubusercontent.com/480644/134466201-8b8b11ad-359d-40ca-87d4-7114ee83cfd3.png">
      </td>
    </tr>
  </tbody>
</table>

## Attempt 5 [With a Dense 512 Layer]
* Pretrained Imagenet Weights
* Inception=>Dropout(0.33)=>Dense(512)=>Dropout(0.33)=>Softmax()
* RandAugment: N=3, M=9
* Epochs: 30 + 70
* Batch Sizes: 128, 128
<table>
  <thead>
    <tr>
      <th align="center" colspan="2">
        Training Summary
        <sub><a href="https://www.dropbox.com/sh/3tjmf0zboiqagvb/AADOOQBL3cWFuSUkbJ_0zh_ga?dl=0">[link]</a></sub>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center" colspan="2">
        <img width="80%" src="https://user-images.githubusercontent.com/480644/134617257-e9e68975-9758-4afd-8564-42fdeb05c200.png">
      </td>
    </tr>
    <tr>
      <td align="center">
        <img width="60%" src="https://user-images.githubusercontent.com/480644/134617501-81f8fe43-e6ee-4900-bfb1-b00fc4d5a44a.png">
      </td>
      <td align="center">
        <img width="60%" src="https://user-images.githubusercontent.com/480644/134617543-dc539bdb-fea2-48ff-9d21-aabc27e4907c.png">
      </td>
    </tr>
    <tr>
      <td align="center" colspan="2">
        <img width="80%" src="https://user-images.githubusercontent.com/480644/134617440-46ee26a1-ccf1-4a21-9dc1-10bb76bb4bc8.png">
      </td>
    </tr>
  </tbody>
</table>

## Attempt 6 [With a Dense 4096 Layer]
* Pretrained Imagenet Weights
* Inception=>Dropout(0.33)=>Dense(4096)=>Dropout(0.33)=>Softmax()
* RandAugment: N=3, M=9
* Epochs: 30, 70
* Batch Sizes: 128, 128
<table>
  <thead>
    <tr>
      <th align="center" colspan="2">
        Training Summary
        <sub><a href="https://www.dropbox.com/sh/o93xwm98yzwlagp/AACJQdgCcuc3S6VnEM3DC3xfa?dl=0">[link]</a></sub>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center" colspan="2">
        <img width="80%" src="https://user-images.githubusercontent.com/480644/134619640-c995cc38-27b2-483b-b70d-d5c6c7c8845a.png">
      </td>
    </tr>
    <tr>
      <td align="right">
        <img width="40%" src="https://user-images.githubusercontent.com/480644/134619777-162440ae-a61f-4963-8f45-fed2670129a3.png">
        <img width="40%" src="https://user-images.githubusercontent.com/480644/134637712-720c8501-1812-4928-a56f-6c754311db69.png">
      </td>
      <td align="left">
        <img width="40%" src="https://user-images.githubusercontent.com/480644/134619857-bfe7ddad-c783-49e5-84c6-d028f65a9e0c.png">
        <img width="40%" src="https://user-images.githubusercontent.com/480644/134637821-4eea7327-0736-4e6f-87be-a53598ee267c.png">
      </td>
    </tr>
    <tr>
      <td align="center" colspan="2">
        <img width="80%" src="https://user-images.githubusercontent.com/480644/134619675-cc5bdaf6-99a1-47ee-b332-32119c4a0fcb.png">
        <img width="80%" src="https://user-images.githubusercontent.com/480644/134637506-cfd3cecc-c0fb-49f4-83e5-1e220bf88c6a.png">
      </td>
    </tr>
  </tbody>
</table>

## Attempt 7 [Image Size: 224]
* Pretrained Imagenet Weights
* Inception=>Softmax()
* RandAugment: N=3, M=9
* Image Size: 224
* Epochs: 30
* Batch Sizes: 128
<table>
  <thead>
    <tr>
      <th align="center" colspan="2">
        Training Summary
        <sub><a href="https://www.dropbox.com/sh/vdj6f9wz2hfjvej/AACZ1aKB6Y3hi5klzUkKCjzXa?dl=0">[link]</a></sub>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center" colspan="2">
        <img width="80%" src="https://user-images.githubusercontent.com/480644/134651371-fea14d5e-5b52-4c4f-bf1c-0b8bfa134c01.png">
      </td>
    </tr>
    <tr>
      <td align="center">
        <img width="60%" src="https://user-images.githubusercontent.com/480644/134651589-96d8f9f5-5775-4c28-b054-e359880f9123.png">
      </td>
      <td align="center">
        <img width="60%" src="https://user-images.githubusercontent.com/480644/134651673-ee19c4d4-538d-4da6-8f9e-9ac8b9780b4a.png">
      </td>
    </tr>
    <tr>
      <td align="center" colspan="2">
        <img width="80%" src="https://user-images.githubusercontent.com/480644/134651494-9830b6ed-0329-478e-819e-2c33877b43a3.png">
      </td>
    </tr>
  </tbody>
</table>

## Attempt 8 [MobileNet, RandAugment]
* Pretrained Imagenet Weights
* MobileNet=>Softmax()
* RandAugment: N=3, M=9
* Image Size: 224
* Epochs: 30
* Batch Sizes: 128
<table>
  <thead>
    <tr>
      <th align="center" colspan="2">
        Training Summary
        <sub><a href="https://www.dropbox.com/sh/ojlzwnpask60w7t/AAD5LnV5HAqPZK8egghXL6y1a?dl=0">[link]</a></sub>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center" colspan="2">
        <img width="80%" src="https://user-images.githubusercontent.com/480644/134656443-c641a413-19ef-49c9-8de4-64afbb64cc94.png">
      </td>
    </tr>
    <tr>
      <td align="center">
        <img width="60%" src="https://user-images.githubusercontent.com/480644/134656643-40ba98fb-27a7-4936-82a4-7f22c9d04757.png">
      </td>
      <td align="center">
        <img width="60%" src="https://user-images.githubusercontent.com/480644/134656726-379ef1e6-a5a7-4cf1-8699-53f5fdcc60e2.png">
      </td>
    </tr>
    <tr>
      <td align="center" colspan="2">
        <img width="80%" src="https://user-images.githubusercontent.com/480644/134656540-eaef7c3d-9da0-4b67-98bd-9a1d7a207d63.png">
      </td>
    </tr>
  </tbody>
</table>

## Attempt 9 [MobileNet]
* Pretrained Imagenet Weights
* MobileNet=>Dropout(0.2)=>Softmax()
* Image Size: 224
* Epochs: 50
* Batch Sizes: 128
<table>
  <thead>
    <tr>
      <th align="center" colspan="2">
        Training Summary
        <sub><a href="https://www.dropbox.com/sh/nnm27njtbvidewi/AAAovznLVqtBCSvS9Xm8G455a?dl=0">[link]</a></sub>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center" colspan="2">
        <img width="80%" src="https://user-images.githubusercontent.com/480644/134924488-cdca22b1-bcd9-44d6-a3dc-9a5a9719317d.png">
      </td>
    </tr>
    <tr>
      <td align="center">
        <img width="60%" src="https://user-images.githubusercontent.com/480644/134925602-d081794e-618d-45b3-b2fa-8d78db8ff292.png">
      </td>
      <td align="center">
        <img width="60%" src="https://user-images.githubusercontent.com/480644/134925732-e5c7396f-cb2a-4c46-9484-d5ba749f881f.png">
      </td>
    </tr>
    <tr>
      <td colspan="2">
<pre>
Epoch 46/50
8/8 [==============================] - 5s 628ms/step - loss: 0.0453 - accuracy: 1.0000 - val_loss: 0.7681 - val_accuracy: 0.8255

Epoch 00046: val_accuracy did not improve from 0.82549
Epoch 47/50
8/8 [==============================] - 5s 628ms/step - loss: 0.0445 - accuracy: 1.0000 - val_loss: 0.7649 - val_accuracy: 0.8235

Epoch 00047: val_accuracy did not improve from 0.82549
Epoch 48/50
8/8 [==============================] - 5s 629ms/step - loss: 0.0412 - accuracy: 1.0000 - val_loss: 0.7619 - val_accuracy: 0.8265

Epoch 00048: val_accuracy improved from 0.82549 to 0.82647, saving model to chkpt/weights-epoch-48-val_accuracy-0.8265.h5
Epoch 49/50
8/8 [==============================] - 5s 632ms/step - loss: 0.0402 - accuracy: 1.0000 - val_loss: 0.7587 - val_accuracy: 0.8235

Epoch 00049: val_accuracy did not improve from 0.82647
Epoch 50/50
8/8 [==============================] - 5s 633ms/step - loss: 0.0407 - accuracy: 1.0000 - val_loss: 0.7556 - val_accuracy: 0.8245

Epoch 00050: val_accuracy did not improve from 0.82647
Uploaded: /mobilenet/chkpt/weights-epoch-48-val_accuracy-0.8265.h5
49/49 [==============================] - 17s 333ms/step - loss: 0.8872 - accuracy: 0.7835
Test accuracy: 78.35%
</pre>
      </td>
    </tr>
  </tbody>
</table>

## Attempt X [...]
<table>
  <thead>
    <tr>
      <th align="center" colspan="2">
        Training Summary
        <sub><a href="">[link]</a></sub>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center" colspan="2">
        <img width="80%" src="">
      </td>
    </tr>
    <tr>
      <td align="center">
        <img width="60%" src="">
        <img width="40%" src="">
      </td>
      <td align="center">
        <img width="60%" src="">
        <img width="40%" src="">
      </td>
    </tr>
    <tr>
      <td align="center" colspan="2">
        <img width="80%" src="">
      </td>
    </tr>
  </tbody>
</table>