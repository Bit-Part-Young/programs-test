# pdf2image

pdf 图片转换 jpg png等格式工具测试

>[GitHub - Belval/pdf2image: A python module that wraps the pdftoppm utility to convert PDF to PIL Image object](https://github.com/Belval/pdf2image)

---

## 安装 pdf2image

- 大多数发行版都带有 `pdftoppm` 和 `pdftocairo`；若未安装，请参考包管理器以安装 `poppler-utils`。

```bash
# 查看是否安装 pdftoppm 和 pdftocairo
which pdftoppm
which pdftocairo

# 安装 poppler-utils
sudo apt install poppler-utils

# 安装 poppler
conda install -c conda-forge poppler
# 安装 pdf2image
pip install pdf2image
```
