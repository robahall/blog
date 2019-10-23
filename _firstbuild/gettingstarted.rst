.. _Getting Started:

Getting started
---------------


For AWS:

*   Sign up for an `AWS Free Tier Account <https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start>`_.


*   Install `Anaconda Python 3.7 <https://www.anaconda.com/distribution/#download-section>`_.


*   Open Terminal in Linux/MacOs or Anaconda Terminal in Windows and create a new environment:

.. code-block:: bash

    conda create -n awsFromScratch anaconda boto3
    conda activate awsFromScratch
    jupyter notebook



.. code-block:: python

    print("Hello World")

