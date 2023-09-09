# mlip intel 版本安装

官方安装 tutorial
>[installation tutorial · Wiki · Alexander Shapeev / MLIP-2 Tutorials · GitLab](https://gitlab.com/ashapeev/mlip-2-tutorials/-/wikis/installation-tutorial)

>[README.md · master · Alexander Shapeev / LAMMPS-MLIP interface · GitLab](https://gitlab.com/ashapeev/interface-lammps-mlip-2/-/blob/master/README.md)


- 先编译 mlip-2，再编译 mlip-2 与 LAMMPS 的接口
- 编译接口时，有多种选项：`intel_cpu_intelmpi`、`g++_mpich`、`mpi`、`g++_serial` 和 `serial` ，编译 `intel_cpu_intelmpi` 版本时，需要在超算中 module load 以下程序
```bash
module load intel-oneapi-compilers/2021.4.0
module load intel-oneapi-mpi/2021.4.0
module load intel-oneapi-mkl/2021.4.0
module load intel-oneapi-tbb/2021.4.0
```

>1. **编译前最好先读 configure、Makefile、install.sh 等配置、编译、安装脚本源代码，了解其默认配置是什么，自定义配置需要修改哪些东西**
>2. arm 无 intel oneapi 套件，pi 和 siyuan 有，建议在后两者平台编译
>3. 建议在编译 mlip-2 开始前，就 module load intel oneapi 套件，因为 `./configure` 命令会自动检测所在平台是否有 mpi，若检测无只会编译串行 serial 版本，后续的接口编译也只能选择串行版本


- 编译接口时，可以在 preinstall.sh 脚本中添加 lammps 需要的 package，可以添加以下 packages
```bash
make yes-basic
make yes-manybody
make yes-KSPACE
# make yes-STUBS
```

>`make yes-STUBS` 不需要添加，因为在 install.sh 脚本中已有 `make mpi-stubs` 选项（本人不知道这两者的区别，也不知道对最终的运行是否会产生影响，**仅从取消该选项后能编译成功得到的判断与猜测**）

>不同版本的 lammps 可以放在同一目录下分别编译，但最后一步会将 lammps 中编译好的 lmp 可执行文件复制到 `interface-lammps-mlip-2` 目录中，其中一个会被覆盖，建议放在不同目录下分别编译



安装情况
- manager 编译 mlip-2 出错，后续无法进行（应该是 2015 版本的 intel 有些老，可以编译 mpi 版本（暂未尝试））
- master 和 siyuan 能编译 2022 版本及最新的稳定版本的 lammps
- arm 编译 mlip-2 出错，后续无法进行（无 intel 程序）




---

## 测试 lammps 2022 版本

- 下载
```bash
wget https://github.com/lammps/lammps/archive/refs/tags/stable_23Jun2022_update4.tar.gz

tar -xzvf stable_23Jun2022_update4.tar.gz

mv lammps-stable_23Jun2022_update4 lammps-stable_23Jun2022
```


- 编译
```bash
./install.sh ../lammps-stable_23Jun2022 intel_cpu_intelmpi

./install.sh ../lammps-stable_23Jun2022 g++_mpich
```




---

## 遇到的问题

### manager 编译 mlip-2 出现错误

```bash
mpiicpc -O3  -I/opt/intel/composer_xe_2015.0.090/mkl/include -MMD  -DMLIP_MPI -DMLIP_INTEL_MKL  -std=c++11 -DMLIP_DEV -c /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.cpp -o /home/yangsl/src/MLIP/mlip-2/obj/mpi/common/bfgs.cpp.o
In file included from /home/yangsl/src/MLIP/mlip-2/src/common/multidimensional_arrays.h(13),
                 from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.h(16),
                 from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.cpp(11):
/usr/include/c++/5/bits/stl_iterator_base_types.h(154): error: class "std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char>>" has no member "iterator_category"
        typedef typename _Iterator::iterator_category iterator_category;
                                    ^
In file included from /home/yangsl/src/MLIP/mlip-2/src/common/multidimensional_arrays.h(13),
                 from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.h(16),
                 from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.cpp(11):
          detected during:
In file included from /home/yangsl/src/MLIP/mlip-2/src/common/multidimensional_arrays.h(13),
                 from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.h(16),
                 from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.cpp(11):
            instantiation of class "std::__iterator_traits<_Iterator, void> [with _Iterator=std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char>>]" at line 163
In file included from /home/yangsl/src/MLIP/mlip-2/src/common/multidimensional_arrays.h(13),
                 from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.h(16),
                 from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.cpp(11):
            instantiation of class "std::iterator_traits<_Iterator> [with _Iterator=std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char>>]" at line 88 of "/home/yangsl/src/MLIP/mlip-2/src/common/utils.h"
In file included from /home/yangsl/src/MLIP/mlip-2/src/common/multidimensional_arrays.h(13),
                 from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.h(16),
                 from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.cpp(11):

In file included from /home/yangsl/src/MLIP/mlip-2/src/common/multidimensional_arrays.h(13),
                 from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.h(16),
                 from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.cpp(11):
/usr/include/c++/5/type_traits(1492): error: class "std::__is_convertible_helper<<error-type>, std::input_iterator_tag, false>" has no member class "type"
      : public __is_convertible_helper<_From, _To>::type
                                                    ^
In file included from /home/yangsl/src/MLIP/mlip-2/src/common/multidimensional_arrays.h(13),
                 from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.h(16),
                 from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.cpp(11):
          detected during instantiation of class "std::is_convertible<_From, _To> [with _From=<error-type>, _To=std::input_iterator_tag]" at line 88 of "/home/yangsl/src/MLIP/mlip-2/src/common/utils.h"
In file included from /home/yangsl/src/MLIP/mlip-2/src/common/multidimensional_arrays.h(13),
                 from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.h(16),
                 from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.cpp(11):

In file included from /home/yangsl/src/MLIP/mlip-2/src/common/multidimensional_arrays.h(13),
                 from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.h(16),
                 from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.cpp(11):
/usr/include/c++/5/type_traits(1492): error: not a class or struct name
      : public __is_convertible_helper<_From, _To>::type
               ^
In file included from /home/yangsl/src/MLIP/mlip-2/src/common/multidimensional_arrays.h(13),
                 from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.h(16),
                 from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.cpp(11):
          detected during instantiation of class "std::is_convertible<_From, _To> [with _From=<error-type>, _To=std::input_iterator_tag]" at line 88 of "/home/yangsl/src/MLIP/mlip-2/src/common/utils.h"
In file included from /home/yangsl/src/MLIP/mlip-2/src/common/multidimensional_arrays.h(13),
                 from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.h(16),
                 from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.cpp(11):

In file included from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.cpp(11):
/usr/include/c++/5/bits/stl_iterator_base_types.h(154): error: class "std::vector<double, std::allocator<double>>" has no member "iterator_category"
        typedef typename _Iterator::iterator_category iterator_category;
                                    ^
In file included from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.cpp(11):
          detected during:
In file included from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.cpp(11):
            instantiation of class "std::__iterator_traits<_Iterator, void> [with _Iterator=std::vector<double, std::allocator<double>>]" at line 163
In file included from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.cpp(11):
            instantiation of class "std::iterator_traits<_Iterator> [with _Iterator=std::vector<double, std::allocator<double>>]" at line 78 of "/home/yangsl/src/MLIP/mlip-2/src/common/multidimensional_arrays.h"
In file included from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.cpp(11):
            instantiation of class "templateArray2D<F> [with F=double]" at line 272 of "/home/yangsl/src/MLIP/mlip-2/src/common/bfgs.h"
In file included from /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.cpp(11):

compilation aborted for /home/yangsl/src/MLIP/mlip-2/src/common/bfgs.cpp (code 2)
/home/yangsl/src/MLIP/mlip-2/make/Makefile:77: recipe for target '/home/yangsl/src/MLIP/mlip-2/obj/mpi/common/bfgs.cpp.o' failed
make: *** [/home/yangsl/src/MLIP/mlip-2/obj/mpi/common/bfgs.cpp.o] Error 2

```



---

### `\r` 错误

master 编译最新版 lammps 出现如下错误。

原因：在 windows 上下载最新版 lammps 源码，再上传到 manager 上，windows 与 linux 之间存在一定的区别，导致如下错误出现。

解决方法：直接下载到 linux 端，速度慢没办法。或者先下载 tar.gz 压缩包到 windows，再上传到 linux 端，勿源码。

```bash
/home/yangsl/src/MLIP-2023/interface-lammps-mlip-2
Uninstalling package user-mlip
Depend.sh: line 3: $'\r': command not found
): No such file or directorysetlocale: LC_ALL: cannot change locale (C
': not a valid identifier: `LC_ALL
Depend.sh: line 7: $'\r': command not found
Depend.sh: line 11: $'\r': command not found
Depend.sh: line 18: $'\r': command not found
Depend.sh: line 22: $'\r': command not found
Depend.sh: line 23: syntax error near unexpected token `$'{\r''
'epend.sh: line 23: `depend () {
make: *** [Makefile:616: no-user-mlip] Error 2
Installing package user-mlip
Depend.sh: line 3: $'\r': command not found
): No such file or directorysetlocale: LC_ALL: cannot change locale (C
': not a valid identifier: `LC_ALL
Depend.sh: line 7: $'\r': command not found
Depend.sh: line 11: $'\r': command not found
Depend.sh: line 18: $'\r': command not found
Depend.sh: line 22: $'\r': command not found
Depend.sh: line 23: syntax error near unexpected token `$'{\r''
'epend.sh: line 23: `depend () {
make: *** [Makefile:600: yes-user-mlip] Error 2
make[1]: Entering directory '/home/yangsl/src/MLIP-2023/mylammps/src'
Installing package kspace
../Install.sh: line 3: $'\r': command not found
../Install.sh: line 7: $'\r': command not found
../Install.sh: line 9: $'\r': command not found
): No such file or directorying: setlocale: LC_ALL: cannot change locale (C
': not a valid identifierxport: `LC_ALL
../Install.sh: line 13: $'\r': command not found
../Install.sh: line 15: $'\r': command not found
../Install.sh: line 16: syntax error near unexpected token `$'{\r''
'./Install.sh: line 16: `action () {
Depend.sh: line 3: $'\r': command not found
): No such file or directorysetlocale: LC_ALL: cannot change locale (C
': not a valid identifier: `LC_ALL
Depend.sh: line 7: $'\r': command not found
Depend.sh: line 11: $'\r': command not found
Depend.sh: line 18: $'\r': command not found
Depend.sh: line 22: $'\r': command not found
Depend.sh: line 23: syntax error near unexpected token `$'{\r''
'epend.sh: line 23: `depend () {
make[1]: *** [Makefile:600: yes-kspace] Error 2
make[1]: Leaving directory '/home/yangsl/src/MLIP-2023/mylammps/src'
make[1]: Entering directory '/home/yangsl/src/MLIP-2023/mylammps/src'
Installing package manybody
../Install.sh: line 3: $'\r': command not found
../Install.sh: line 7: $'\r': command not found
../Install.sh: line 9: $'\r': command not found
): No such file or directorying: setlocale: LC_ALL: cannot change locale (C
': not a valid identifierxport: `LC_ALL
../Install.sh: line 13: $'\r': command not found
../Install.sh: line 15: $'\r': command not found
../Install.sh: line 16: syntax error near unexpected token `$'{\r''
'./Install.sh: line 16: `action () {
Depend.sh: line 3: $'\r': command not found
): No such file or directorysetlocale: LC_ALL: cannot change locale (C
': not a valid identifier: `LC_ALL
Depend.sh: line 7: $'\r': command not found
Depend.sh: line 11: $'\r': command not found
Depend.sh: line 18: $'\r': command not found
Depend.sh: line 22: $'\r': command not found
Depend.sh: line 23: syntax error near unexpected token `$'{\r''
'epend.sh: line 23: `depend () {
make[1]: *** [Makefile:600: yes-manybody] Error 2
make[1]: Leaving directory '/home/yangsl/src/MLIP-2023/mylammps/src'
make[1]: Entering directory '/home/yangsl/src/MLIP-2023/mylammps/src'
Installing package molecule
../Install.sh: line 3: $'\r': command not found
../Install.sh: line 7: $'\r': command not found
../Install.sh: line 9: $'\r': command not found
): No such file or directorying: setlocale: LC_ALL: cannot change locale (C
': not a valid identifierxport: `LC_ALL
../Install.sh: line 13: $'\r': command not found
../Install.sh: line 15: $'\r': command not found
../Install.sh: line 16: syntax error near unexpected token `$'{\r''
'./Install.sh: line 16: `action () {
Depend.sh: line 3: $'\r': command not found
): No such file or directorysetlocale: LC_ALL: cannot change locale (C
': not a valid identifier: `LC_ALL
Depend.sh: line 7: $'\r': command not found
Depend.sh: line 11: $'\r': command not found
Depend.sh: line 18: $'\r': command not found
Depend.sh: line 22: $'\r': command not found
Depend.sh: line 23: syntax error near unexpected token `$'{\r''
'epend.sh: line 23: `depend () {
make[1]: *** [Makefile:600: yes-molecule] Error 2
make[1]: Leaving directory '/home/yangsl/src/MLIP-2023/mylammps/src'
make[1]: Entering directory '/home/yangsl/src/MLIP-2023/mylammps/src'
Installing package rigid
../Install.sh: line 3: $'\r': command not found
../Install.sh: line 7: $'\r': command not found
../Install.sh: line 9: $'\r': command not found
): No such file or directorying: setlocale: LC_ALL: cannot change locale (C
': not a valid identifierxport: `LC_ALL
../Install.sh: line 13: $'\r': command not found
../Install.sh: line 15: $'\r': command not found
../Install.sh: line 16: syntax error near unexpected token `$'{\r''
'./Install.sh: line 16: `action () {
Depend.sh: line 3: $'\r': command not found
): No such file or directorysetlocale: LC_ALL: cannot change locale (C
': not a valid identifier: `LC_ALL
Depend.sh: line 7: $'\r': command not found
Depend.sh: line 11: $'\r': command not found
Depend.sh: line 18: $'\r': command not found
Depend.sh: line 22: $'\r': command not found
Depend.sh: line 23: syntax error near unexpected token `$'{\r''
'epend.sh: line 23: `depend () {
make[1]: *** [Makefile:600: yes-rigid] Error 2
make[1]: Leaving directory '/home/yangsl/src/MLIP-2023/mylammps/src'
make: *** [Makefile:574: yes-basic] Error 2
Installing package manybody
../Install.sh: line 3: $'\r': command not found
../Install.sh: line 7: $'\r': command not found
../Install.sh: line 9: $'\r': command not found
): No such file or directorying: setlocale: LC_ALL: cannot change locale (C
': not a valid identifierxport: `LC_ALL
../Install.sh: line 13: $'\r': command not found
../Install.sh: line 15: $'\r': command not found
../Install.sh: line 16: syntax error near unexpected token `$'{\r''
'./Install.sh: line 16: `action () {
Depend.sh: line 3: $'\r': command not found
): No such file or directorysetlocale: LC_ALL: cannot change locale (C
': not a valid identifier: `LC_ALL
Depend.sh: line 7: $'\r': command not found
Depend.sh: line 11: $'\r': command not found
Depend.sh: line 18: $'\r': command not found
Depend.sh: line 22: $'\r': command not found
Depend.sh: line 23: syntax error near unexpected token `$'{\r''
'epend.sh: line 23: `depend () {
make: *** [Makefile:600: yes-manybody] Error 2
Installing package KSPACE
../Install.sh: line 3: $'\r': command not found
../Install.sh: line 7: $'\r': command not found
../Install.sh: line 9: $'\r': command not found
): No such file or directorying: setlocale: LC_ALL: cannot change locale (C
': not a valid identifierxport: `LC_ALL
../Install.sh: line 13: $'\r': command not found
../Install.sh: line 15: $'\r': command not found
../Install.sh: line 16: syntax error near unexpected token `$'{\r''
'./Install.sh: line 16: `action () {
Depend.sh: line 3: $'\r': command not found
): No such file or directorysetlocale: LC_ALL: cannot change locale (C
': not a valid identifier: `LC_ALL
Depend.sh: line 7: $'\r': command not found
Depend.sh: line 11: $'\r': command not found
Depend.sh: line 18: $'\r': command not found
Depend.sh: line 22: $'\r': command not found
Depend.sh: line 23: syntax error near unexpected token `$'{\r''
'epend.sh: line 23: `depend () {
make: *** [Makefile:600: yes-KSPACE] Error 2
make[1]: Entering directory '/home/yangsl/src/MLIP-2023/mylammps/src/STUBS'
rm -f *.o libmpi_stubs.a
make[1]: Leaving directory '/home/yangsl/src/MLIP-2023/mylammps/src/STUBS'
make[1]: Entering directory '/home/yangsl/src/MLIP-2023/mylammps/src/STUBS'
g++ -O -fPIC -I.  -c mpi.cpp
ar rs libmpi_stubs.a mpi.o
ar: creating libmpi_stubs.a
make[1]: Leaving directory '/home/yangsl/src/MLIP-2023/mylammps/src/STUBS'
Gathering installed package information (may take a little while)
Make.sh: line 7: $'\r': command not found
): No such file or directoryetlocale: LC_ALL: cannot change locale (C
': not a valid identifier `GREP_OPTIONS
Make.sh: line 13: $'\r': command not found
Make.sh: line 15: $'\r': command not found
Make.sh: line 16: syntax error near unexpected token `$'{\r''
'ake.sh: line 16: `style () {
make: *** [Makefile:384: intel_cpu_intelmpi] Error 2
cp: cannot stat '../mylammps/src/lmp_intel_cpu_intelmpi': No such file or directory

```




---

### 在 arm 平台编译接口，load openmpi/4.1.1-gcc-9.3.0 程序，提示找不到相关共享链接库

**解决方法：建议不在 arm 平台编译，arm 平台可 module load 程序少且有些旧。**

```bash
mpicxx -O3 -I./cblas -MMD -DMLIP_MPI -std=c++11 -DMLIP_DEV -c /lustre/home/acct-mseklt/mseklt/yangsl/software/mlip-2/src/common/bfgs.cpp -o /lustre/home/acct-mseklt/mseklt/yangsl/software/mlip-2/obj/mpi/common/bfgs.cpp.o
mpicxx: error while loading shared libraries: libpmi2.so.0: cannot open shared object file: No such file or directory
make: *** [/lustre/home/acct-mseklt/mseklt/yangsl/software/mlip-2/obj/mpi/common/bfgs.cpp.o] Error 127
```



---

### 编译 intel_cpu_intelmpi 版本，load mpich/3.3.2-intel-19.0.5 程序，提示未找到 `mpiicpc` 命令

**解决方法：应 load intel-oneapi 程序套件**

```bash
cc -O -o fastdep.exe ../DEPEND/fastdep.c
make[1]: Leaving directory `/lustre/home/acct-mseklt/mseklt/yangsl/softwares/pi-softwares/mylammps/src/Obj_intel_cpu_intelmpi'
make[1]: Entering directory `/lustre/home/acct-mseklt/mseklt/yangsl/software/pi-softwares/mylammps/src/Obj_intel_cpu_intelmpi'
mpiicpc -std=c++11 -diag-disable=10441 -diag-disable=2196 -qopenmp -qno-offload -ansi-alias -restrict -DLMP_INTEL_USELRT -DLMP_USE_MKL_RNG -xHost -O2 -fp-model fast=2 -no-prec-div -qoverride-limits -qopt-zmm-usage=high -I/include -DLAMMPS_GZIP -I../../lib/mlip -DMPICH_SKIP_MPICXX -DOMPI_SKIP_MPICXX=1 -DFFT_MKL -DFFT_SINGLE -lgfortran -c ../main.cpp
/lustre/opt/cascadelake/linux-centos7-cascadelake/gcc-11.2.0/intel-oneapi-mpi-2021.6.0-xyxek2osiqlzbkvzgysroekj2zdfhcg2/mpi/2021.6.0/bin/mpiicpc: line 558: icpc: command not found
make[1]: *** [main.o] Error 127
make[1]: Leaving directory `/lustre/home/acct-mseklt/mseklt/yangsl/software/pi-softwares/mylammps/src/Obj_intel_cpu_intelmpi'
make: *** [intel_cpu_intelmpi] Error 2
cp: cannot stat '../mylammps/src/lmp_intel_cpu_intelmpi': No such file or directory
```



---

### 脚本 preinstall.sh 中添加 `make yes-STUBS` 选项，编译 `g++_mpich` 和 `intel_cpu_intelmpi` 版本版本时，提示找不到 `../version.h` 头文件

**解决方法：取消 `make yes-STUBS` 选项。**

```bash
../mpi.cpp:18:24: fatal error: ../version.h: No such file or directory
 #include "../version.h"
                        ^
compilation terminated.
make[1]: *** [mpi.o] Error 1
make[1]: Leaving directory `/lustre/home/acct-mseklt/mseklt/yangsl/software/pi-softwares/mylammps/src/Obj_g++_mpich'
make: *** [g++_mpich] Error 2
cp: cannot stat '/lustre/home/acct-mseklt/mseklt/yangsl/software/pi-softwares/mylammps/src/lmp_g++_mpich': No such file or directory
```


lammps 目录下 `../version.h` 可能所在的目录路径
```bash
❯ rg '../version.h'
doc/src/Manual_version.rst
30:run LAMMPS. It is also in the file src/version.h and in the LAMMPS

examples/PACKAGES/pace/plugin/CMakeLists.txt
35: get_lammps_version(${LAMMPS_SOURCE_DIR}/version.h LAMMPS_VERSION)

src/STUBS/Makefile
44:$(OBJ):      $(INC) ../version.h

src/STUBS/mpi.cpp
18:#include "../version.h"

src/mpi.cpp
18:#include "../version.h"

cmake/CMakeLists.txt
84:get_lammps_version(${LAMMPS_SOURCE_DIR}/version.h PROJECT_VERSION)
882:    file(COPY ${LAMMPS_SOURCE_DIR}/version.h DESTINATION ${CMAKE_BINARY_DIR}/python/src)
```



---

### 编译 `lmp_intel_cpu_intelmpi` 版本，load intel-oneapi-compiler、mpi、mkl 程序，提示未找到 `tbbmalloc` 链接库

**解决方法：还要 load tbb 程序。**

```bash
mpiicpc -std=c++11 -diag-disable=10441 -diag-disable=2196 -qopenmp -xHost -O2 -fp-model fast=2 -no-prec-div -qoverride-limits -qopt-zmm-usage=high -L/dssg/opt/icelake/linux-centos8-icelake/gcc-8.5.0/intel-oneapi-mkl-2021.4.0-r7h6alnulyzgb6iqvxhovmwrajvwbqxf/mkl/2021.4.0/lib/intel64/ main.o -L../../lib/mlip       -L. -llammps_intel_cpu_intelmpi -l_mlip_interface     -std=c++11 -lgfortran  -ldl -ltbbmalloc -lmkl_intel_ilp64 -lmkl_sequential -lmkl_core   -o ../lmp_intel_cpu_intelmpi
ld: cannot find -ltbbmalloc
make[1]: *** [Makefile:98: ../lmp_intel_cpu_intelmpi] Error 1
make[1]: Leaving directory '/dssg/home/acct-mseklt/mseklt/yangsl/src/MLIP/lammps-stable_23Jun2022/src/Obj_intel_cpu_intelmpi'
make: *** [Makefile:393: intel_cpu_intelmpi] Error 2
cp: cannot stat '../lammps-stable_23Jun2022/src/lmp_intel_cpu_intelmpi': No such file or directory

```



---

### 编译成功

- `g++_mpich` 版本
```bash
mpicxx -cxx=g++ -g -O -std=c++11 main.o -L../../lib/mlip -L. -llammps_g++_mpich -l_mlip_interface -std=c++11 -lgfortran -ldl -o ../lmp_g++_mpich
size ../lmp_g++_mpich
   text data bss dec hex filename
6073025 12712 11280 6097017 5d0879 ../lmp_g++_mpich
make[1]: Leaving directory `/lustre/home/acct-mseklt/mseklt/yangsl/software/pi-softwares/lammps-stable_23Jun2022/src/Obj_g++_mpich'

```


- `intel_cpu_intelmpi` 版本
```bash
mpiicpc -std=c++11 -diag-disable=10441 -diag-disable=2196 -qopenmp -xHost -O2 -fp-model fast=2 -no-prec-div -qoverride-limits -qopt-zmm-usage=high -L/dssg/opt/icelake/linux-centos8-icelake/gcc-8.5.0/intel-oneapi-mkl-2021.4.0-r7h6alnulyzgb6iqvxhovmwrajvwbqxf/mkl/2021.4.0/lib/intel64/ main.o -L../../lib/mlip       -L. -llammps_intel_cpu_intelmpi -l_mlip_interface     -std=c++11 -lgfortran  -ldl -ltbbmalloc -lmkl_intel_ilp64 -lmkl_sequential -lmkl_core   -o ../lmp_intel_cpu_intelmpi
size ../lmp_intel_cpu_intelmpi
   text    data     bss     dec     hex filename
13436817         242936   14280 13694033         d0f451 ../lmp_intel_cpu_intelmpi
make[1]: Leaving directory '/dssg/home/acct-mseklt/mseklt/yangsl/src/MLIP/lammps-stable_23Jun2022/src/Obj_intel_cpu_intelmpi'

```



---

### 编译被 kill

登录节点出现崩溃，编译被 kill，请在申请节点上编译。

```bash
icpc: error #10106: Fatal error in /lustre/opt/cascadelake/linux-centos7-cascadelake/gcc-9.2.0/intel-oneapi-compilers-2021.4.0-4zbionrhsiw4f7bcjrtmuoorpwwrqj5r/compiler/2021.4.0/linux/bin/intel64/../../bin/intel64/mcpcom, terminated by kill signal
compilation aborted for ../create_atoms.cpp (code 1)
make[1]: *** [create_atoms.o] Error 1
make[1]: Leaving directory `/lustre/home/acct-mseklt/mseklt/yangsl/softwares/pi-softwares/lammps-stable_23Jun2022/src/Obj_intel_cpu_intelmpi'
make: *** [intel_cpu_intelmpi] Error 2
cp: cannot stat ‘/lustre/home/acct-mseklt/mseklt/yangsl/softwares/pi-softwares/lammps-stable_23Jun2022/src/lmp_intel_cpu_intelmpi’: No such file or directory

```
