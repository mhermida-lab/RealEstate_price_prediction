{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "def read_shapefile(sf):\n",
    "    #fetching the headings from the shape file\n",
    "    fields = [x[0] for x in sf.fields][1:]\n",
    "#fetching the records from the shape file\n",
    "    records = [list(i) for i in sf.records()]\n",
    "    shps = [s.points for s in sf.shapes()]\n",
    "#converting shapefile data into pandas dataframe\n",
    "    df = pd.DataFrame(columns=fields, data=records)\n",
    "#assigning the coordinates\n",
    "    df_shape = df.assign(coords=shps)\n",
    "    return df_shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
 "nbformat_minor": 2
}
