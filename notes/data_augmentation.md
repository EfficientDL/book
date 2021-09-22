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

## Attempt X [...]
<table>
  <thead>
    <tr>
      <th align="center" colspan="2">Training Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><img width="60%" src=""></td>
      <td align="center"><img width="60%" src=""></td>
    </tr>
    <tr>
      <td align="center" colspan="2"><img width="80%" src=""></td>
    </tr>
  </tbody>
</table>



[Attempt 1 Accuracy]: https://user-images.githubusercontent.com/480644/134125333-cdeea1d4-bfd6-4790-9287-acf2174d4872.png
[Attempt 1 Loss]: https://user-images.githubusercontent.com/480644/134125400-40f87081-73d2-4fde-bbf0-f8491cd35535.png
[Attempt 1 Training]: https://user-images.githubusercontent.com/480644/134125025-fe9617cf-3ab1-4fe7-9612-5ba95302205a.png
