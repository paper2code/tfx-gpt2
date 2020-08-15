# Finetune GPT-2 with TFX Pipeline
Main work done by [nsheppert/gpt-2](https://github.com/nshepperd/gpt-2)

In this repository, we take the existing code and transform it into a TFX pipeline. The TFX pipeline can then be orchestrated with either Airflow or Kubeflow. Have a look at `examples` for getting to know how to use this module.

## TODO
- create custom component for encode.py
- create custom component for train.py
- initialize components with create_components
- initialize pipeline  with create_pipeline