Hola this is a test for a table:

| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |


| Time | Parallel-mode | Nodes | Threads | Script | Output |
| ---- | ------------- | ----- | ------- | ------ | ------ |
| 4m58.887s | Pure MPI | 2 | 1 | job01.sl | job01.out |
| 2m29.097s | Pure MPI | 4 | 1 | job02.sl | job02.out |
| 1m17.383s | Pure MPI | 8 | 1 | job03.sl | job03.out |
| 0m36.114s | Pure MPI | 16 | 1 | job04.sl | job04.out |
| ERROR | Pure MPI | 32 | 1 | job05.sl | job05.out |
| ----- | -------- | --- | --- | --- | ---------- |
