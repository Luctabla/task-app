Requirements
************

* Python 3.8.1
* Django 3.1.2
* Django-REST-Framework 3.12.2
* djangorestframework-datatables 0.6.0

Installation on Linux-Ubuntu 18.04
**********************************

First we will create a virtual environment to isolate resources using virtualenv.
To use the virtual environment install virtualenv, as a requirement you must have pip installed.

Setting the enviroment
======================

Installing Pip
--------------
.. code-block:: console
   
   sudo apt-get install python3-pip
   
Installing virtualenv
---------------------
.. code-block:: console
   
   python3 -m pip install virtualenv

Create and activate the virtual enviroment
------------------------------------------
.. code-block:: console

   virtualenv sw-env -p python3
   source sw-env/bin/activate

Starting the project
====================

Installing Project's requirements
---------------------------------
Within the root of the star_wars project run:
.. code-block:: console
   
   pip3 install -r requirements.txt

Running migrations
------------------
.. code-block:: console 
 
   python manage.py migrate --run-syncdb

Running Server
--------------
.. code-block:: console
   
   python manage.py runserver 0.0.0.0:8000

Structure (Endpoints)
=====================

=============================  ===========  ===========  ============  ==============
Endpoint                       HTTP Method  CRUD Method  Result        Authentication
                                                                       is required
=============================  ===========  ===========  ============  ==============
/register/                     POST         Write        Create a new  No
                                                         user
/auth/login/                   POST         Read         Login user    No
/tasks/                        GET          Read         List user's   Yes
                                                         tasks
/tasks/                        POST         Create       Create a new  Yes
                                                         task
/api/tasks/$id/                PUT          Update       Update task   Yes
/api/tasks/$id/                DELETE       Delete       Delete task   Yes


=============================  ===========  ===========  ============  ==============

Tests
*****
Running tests
=============

In order to run the tests you have run 

.. code-block:: console
    
   python manage.py test
