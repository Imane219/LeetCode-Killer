# LeetCode-Killer
Recording tackled/to be tackled leetcode problems and summarizing the key takeaways.



Following the problems sequence of [leetcode-master](https://github.com/youngyangyang04/leetcode-master). 



## Context







## Timeline

| Date                  | Problems                                                     | Done                                                         |
| --------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Sep.2nd - Sep.5th     | **List:** 704,27,977,209,59                                  | 9.6 - 704，9.7 - 27, 9.11 - 977, 10.12-209,59                |
| Sep.6th - Sep.11th    | **Linked List:** 203,707,206,24,19,160,142                   | 10.13-203,10.15-707 206，10.16-24,10.17-19，160, 10.18-142   |
| Sep.11th - Sep.15th   | **Hash map:** 242,1002,349,202,1,454,383,15,18               | 10.20-242，10.21-1002，10.22-349,202,1,10.23-454,383,10.24-15,10.25-18 |
| Sep.16th - Sep.21th   | **String:** 344,541,05(剑指Offer),151,58-2(Offer),28,459     | 10.26-344,541,05,58-2,10.31-28,11.1-459                      |
| Sep.22th - Sep.25th   | **Double pointer:** 27,344,05(Offer),151,206,19,160,142,15,18 | 11.5                                                         |
| Sep.25th - Sep.30th   | **Stack and Queue:** 232,225,20,1047,150,239,347             | 11.6-232,11.8-225,11.9-20,1047,150; 11.10-239;11.11-347;     |
|                       | **Binary tree:** 144,145,94,102                              | 11.14-102,11.15-226,589,101,111,11.16-222;11.18-110;12.11-617;12.12-700,98,530,501,236;12.17-235,701,450，669，108，538 |
| 12.18-12.25           | **Trace Back**                                               | 12.18-77;12.19-216,12.20-17,39,40;12.21-131,93,78;12.22-90,491,46,47;12.25-332,51,37 |
| 12.26-12.30           | **Greedy algorithm**                                         | 12.26-455,376,53;12.27-122,55,45,1005;12.28-134,135,860,406;1.1-452,435,763,56,738,968 |
| 1.2-1.6               | **DP1**                                                      | 1.2-509,70,746;1.3-62;1.4-63;1.5-343;1.6-96                  |
| 1.7-1.10              | **DP2, backpack, house robber**                              | 1.9-416;1.11-1049;1.13-494,474;11.14-518;1.17-377;1.18-70,322,279;1.20-198,213,337 |
| 1.22                  | **trade stocks**                                             | 1.22-121;2.5-188,123;2.6-309,714                             |
| 2.6                   | **LCS**                                                      | 2.6-1143,72,300,674; 2.9-718,1035,392,115,583,647,516        |
| 2.10                  | **hot100**                                                   | 2.10-88,26,80,169,189                                        |
| hot-100 and 剑指offer |                                                              |                                                              |
| codetop面试热题       |                                                              |                                                              |







Pretrained model:

- pretraining method: baseline
- pretrained dataset: mini-imagenet.train

Adv generator:

- training set: cifarfs.train
- optimization:
  - optimzier: adam
  - lr: 0.0002
  - epoch: 20
  - loss: follow the iccv23

Test:

- dataset: mini-imagenet.test
- classifier: linear with 100 epoch's finetuning
- accuracy:
  - fs clean: 1-shot and 5-shot
  - fs adv: 1-shot and 5-shot
  - attack success rate(asr): 1-shot and 5-shot

