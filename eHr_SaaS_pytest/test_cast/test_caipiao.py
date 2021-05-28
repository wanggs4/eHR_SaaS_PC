import random

# “双色球”每注投注号码由6个红色球号码和1个蓝色球号码组成。红色球号码从1--33中选择；蓝色球号码从1--16中选择1
def test_random_dual_colored_ball():
    red_ball = random.sample(list(range(1,34)),6)
    red_ball.sort()
    blue_ball = random.sample(list(range(1,17)),1)
    result_ball = (red_ball,blue_ball)
    print('当前预测双色球结果如下：{}'.format(result_ball))
    print('红球：{}   蓝球：{}'.format(result_ball[0],result_ball[1]))
