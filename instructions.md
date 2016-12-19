# Project install instructions

## Setup

### Create virtualenvironment for python

`virtualenv -p python3 virtualenv.wsdproject`

### Activate virtualenv (assuming we are on root of this repo and virtualenv is one step above)
`. ../virtualenv.wsdproject/bin/activate`

### install required python modules

`pip install --upgrade pip`

`pip install -r requirements.txt`

run `./manage.py migrate`

`mkdir logs`

you should be now have succesfully setup dev-env

## Running

### Activate virtualenv 

assuming we are on root of this repo and virtualenv is one step above:

`. ../virtualenv.wsdproject/bin/activate`

### use runserver command
`./manage.py runserver`

