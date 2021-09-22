We used a bare inception model to train on the oxford flowers dataset. The dataset has 1020 training, 1020 validation and 6149 test examples.

<img src="https://user-images.githubusercontent.com/480644/134114129-488002ca-37cc-41c0-9df9-d3626da4de2f.png" width="50%">

It has 102 distinct flower labels. Each image is assigned a unique label.

We experimented with several data augmentation techniques. The results are described in the later sections. All the experiments are run with the following prameters unless otherwise stated:
* Base Model: Inception
* Epochs: 30
* Batch Size: 64

## Attempt 1
### Training Summary
<table>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/480644/134125333-cdeea1d4-bfd6-4790-9287-acf2174d4872.png"></td>
    <td><img src="https://user-images.githubusercontent.com/480644/134125400-40f87081-73d2-4fde-bbf0-f8491cd35535.png"></td>
  </tr>
  <tr>
    <td colspan="2"><img src="https://user-images.githubusercontent.com/480644/134125025-fe9617cf-3ab1-4fe7-9612-5ba95302205a.png"></td>
  </tr>
</table>

## Attempt 2 [Pretrained Weights]
<table>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/480644/134286439-6dc30cf0-06e1-4ae9-bf07-7347130fa837.png"></td>
    <td><img src="https://user-images.githubusercontent.com/480644/134286492-ef1e5ba3-6618-4465-b3f3-14ca8c378f9f.png"></td>
  </tr>
  <tr>
    <td colspan="2"><img src="https://user-images.githubusercontent.com/480644/134286368-eff2f839-cf62-431c-b0a5-c97f5026a93f.png"></td>
  </tr>
</table>

## Attempt X [...]
<table>
  <tr>
    <td><img src=""></td>
    <td><img src=""></td>
  </tr>
  <tr>
    <td colspan="2"><img src=""></td>
  </tr>
</table>



[Attempt 1 Accuracy]: https://user-images.githubusercontent.com/480644/134125333-cdeea1d4-bfd6-4790-9287-acf2174d4872.png
[Attempt 1 Loss]: https://user-images.githubusercontent.com/480644/134125400-40f87081-73d2-4fde-bbf0-f8491cd35535.png
[Attempt 1 Training]: https://user-images.githubusercontent.com/480644/134125025-fe9617cf-3ab1-4fe7-9612-5ba95302205a.png
