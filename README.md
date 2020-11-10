# boxplot

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme) ![standard-readme compliant](https://img.shields.io/badge/complete-100%25-green) ![GitHub](https://img.shields.io/github/license/HurryZhao/boxplot) ![GitHub watchers](https://img.shields.io/github/watchers/HurryZhao/boxplot?style=social)

## Table of Contents

- [Background](#background)
- [Files](#files)
- [Install](#install)
- [Usage](#usage)
- [Badge](#badge)
- [Related Efforts](#related-efforts)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Background

As a project of course **Information Visualization**.

The goals for this repository are:

1. A well defined **method**. This can be imported and used to generate different types of box plot .
2. **A Report**. It documents the different types of *boxplots* and explain how to use the methods we have created, while illustrating with plots generated with our work..
3. A **Jupyter Noyerbook file** for users as a user guide.



## Files

- [IV_Project1.ipynb](https://github.com/HurryZhao/boxplot/blob/master/IV_Project1.ipynb) The original file for the box plot method.
- [code](https://github.com/HurryZhao/boxplot/tree/master/code)
  - [boxplot.py](https://github.com/HurryZhao/boxplot/blob/master/code/boxplot.py) The module used to draw box plots
  - [test.ipynb](https://github.com/HurryZhao/boxplot/blob/master/code/test.ipynb) The file to test the module
  - [main.py](https://github.com/HurryZhao/boxplot/blob/master/code/main.py) An example how to use the module
- [results_merged.csv](https://github.com/HurryZhao/boxplot/blob/master/results_merged.csv) The dataset we used

## Install

This project can only be installed by cloning this git.

```sh
$ git clone https://github.com/HurryZhao/boxplot.git
```

## Usage

import the `boxplot.py` as a module and use the method. Following is an example:

```python
from boxplot import boxplot as bp

data = [[...],[...]]

fig,ax=matplotlib.pyplot.subplots()
bx.boxplot(ax,data)
```

## Badge



- README style:[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

- Completeness:![standard-readme compliant](https://img.shields.io/badge/complete-100%25-green)

- License: ![GitHub](https://img.shields.io/github/license/HurryZhao/boxplot)

- Watchers: ![GitHub watchers](https://img.shields.io/github/watchers/HurryZhao/boxplot?style=social)

## Related Efforts

- [android_test_inspector](https://github.com/luiscruz/android_test_inspector) Delivered a dataset available.

## Maintainers

[@HurryZhao](https://github.com/HurryZhao)

[@Coolplaybaobao](https://github.com/Coolplaybaobao)

## Contributing

Feel free to dive in! [Open an issue](https://github.com/HurryZhao/boxplot/issues) or submit PRs.

### Contributors

[@HurryZhao](https://github.com/HurryZhao)

[@Coolplaybaobao](https://github.com/Coolplaybaobao)

## License

[MIT](LICENSE) © 2020 Zhao Haoran
