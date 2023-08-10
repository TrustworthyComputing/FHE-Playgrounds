`Integer (4)`
```powershell
java -jar target/terminator-compiler-1.0.jar \
src/test/resources/logistic_regression/logistic_regression_a4.t2 --SEAL \
--config src/test/resources/logistic_regression/configs/seal-bfv-16k-128-int.config
```

`Floating Point (4)`
```powershell
java -jar target/terminator-compiler-1.0.jar \
src/test/resources/logistic_regression/logistic_regression_a4_fp.t2 --SEAL \
--config src/test/resources/logistic_regression/configs/seal-ckks-16k-128-fp.config
```
