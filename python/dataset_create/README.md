# Dataset_create
## 1、生成工具依赖包

（1）sklearn

（2）numpy

（3）pandas

安装方式：

```python
pip install numpy pandas sklearn
```

## 2、工具参数说明

修改dataset_create.py中 make_classification 函数入参, 具体参数说明如下：



| **参数**             | **类型**                                   | **默认**                 | **说明**                                                     |
| -------------------- | ------------------------------------------ | ------------------------ | ------------------------------------------------------------ |
| n_samples            | int类型                                    | 可选 (default=100)       | 样本数量.                                                    |
| n_features           | int                                        | 可选 (default=20)        | 总的特征数量,是从有信息的数据点，冗余数据点，重复数据点，和特征点-有信息的点-冗余的点-重复点中随机选择的。 |
| n_informative        | int                                        | optional  (default=2)    | informative  features数量                                    |
| n_redundant          | int                                        | optional  (default=2)    | redundant  features数量                                      |
| n_repeated           | int                                        | optional  (default=0)    | duplicated  features数量                                     |
| n_classes            | int                                        | optional  (default=2)    | 类别或者标签数量                                             |
| n_clusters_per_class | int                                        | optional  (default=2)    | 每个class中cluster数量                                       |
| weights              | floats列表 or None                         | (default=None)           | 每个类的权重，用于分配样本点                                 |
| flip_y               | float                                      | optional  (default=0.01) | 随机交换样本的一段                                           |
| class_sep            | float                                      | optional  (default=1.0)  | The  factor multiplying the hypercube dimension.             |
| hypercube            | boolean                                    | optional  (default=True) | If  True the clusters are put on the vertices of a hypercube. If False,the  clusters are put on the vertices of a random polytope. |
| shift                | float,array  of shape [n_features] or None | optional  (default=0.0)  | Shift  features by the specified value. If None,then features are shifted by a  random value drawn in [-class_sep,class_sep]. |
| scale                | float  array of shape [n_features] or None | optional  (default=1.0)  | Multiply  features by the specified value. If None,then features are scaled by a random  value drawn in [1,100]. Note that scaling happens after shifting. |
| shuffle              | boolean                                    | optional  (default=True) | Shuffle  the samples and the features.                       |
| random_state         | int,RandomState  instance or None          | optional  (default=None) | If  int,random_state is the seed used by the random number generator; If  RandomState instance,random_state is the random number generator; If None,the  random number generator is the RandomState instance used by np.random |
|                      |                                            |                          |                                                              |

 

## 3、工具执行产出

（1）产出文件：dataset.csv

（2）文件格式：csv

（3）特征名：x1-xN

（4）标签名：y
