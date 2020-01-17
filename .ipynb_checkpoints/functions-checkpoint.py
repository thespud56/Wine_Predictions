{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#  Import statements\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import missingno\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from scipy import stats\n",
    "from IPython.display import display_html\n",
    "\n",
    "\n",
    "def clean_df(raw_df):\n",
    "    '''Function that removes duplicate wines, unwanted columns, naans, and wines above $100'''\n",
    "    nodup_df = raw_df.duplicated(subset='title', keep='first')\n",
    "    nodup_df = raw_df[nodup_df].drop(['Unnamed: 0', 'designation', 'region_1', 'region_2'], axis=1)\n",
    "    nodup_df = nodup_df.dropna()\n",
    "    df = nodup_df[nodup_df['price'] >= 100 ].index\n",
    "    nodup_df.drop(df, inplace=True)\n",
    "    return nodup_df"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
