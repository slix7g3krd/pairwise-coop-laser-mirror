# pairwise-coop-laser-mirror

## 领域

游戏、图形与多媒体

## 主题

多人协作激光反射解谜同步

## 说明

镜面角度权威插值、反射深度统一、注册与渲染栅栏。

初始状态下 `game/laser_optics.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
