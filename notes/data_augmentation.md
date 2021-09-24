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
      <th align="center" colspan="2">Training Summary</th>
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
      <th align="center" colspan="2">Training Summary</th>
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
* Epochs: 30
* Batch Sizes: 128
<table>
  <thead>
    <tr>
      <th align="center" colspan="2">Training Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center" colspan="2">
        <img width="80%" src="https://user-images.githubusercontent.com/480644/134619640-c995cc38-27b2-483b-b70d-d5c6c7c8845a.png">
      </td>
    </tr>
    <tr>
      <td align="center">
        <img width="60%" src="https://user-images.githubusercontent.com/480644/134619777-162440ae-a61f-4963-8f45-fed2670129a3.png">
      </td>
      <td align="center">
        <img width="60%" src="https://user-images.githubusercontent.com/480644/134619857-bfe7ddad-c783-49e5-84c6-d028f65a9e0c.png">
      </td>
    </tr>
    <tr>
      <td align="center" colspan="2">
        <img width="80%" src="https://user-images.githubusercontent.com/480644/134619675-cc5bdaf6-99a1-47ee-b332-32119c4a0fcb.png">
      </td>
    </tr>
  </tbody>
</table>

## Attempt X [...]
<table>
  <thead>
    <tr>
      <th align="center" colspan="2">Training Summary</th>
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



[Attempt 1 Accuracy]: https://user-images.githubusercontent.com/480644/134125333-cdeea1d4-bfd6-4790-9287-acf2174d4872.png
[Attempt 1 Loss]: https://user-images.githubusercontent.com/480644/134125400-40f87081-73d2-4fde-bbf0-f8491cd35535.png
[Attempt 1 Training]: https://user-images.githubusercontent.com/480644/134125025-fe9617cf-3ab1-4fe7-9612-5ba95302205a.png
