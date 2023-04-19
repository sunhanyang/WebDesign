# 实验3：对实验1的oop实现


class person:
    def __init__(self, salary, year, house):
        self.salary = salary  # 初始工资
        self.year = year  # 工作年份
        self.salary_per_year = []  # 每年薪资统计 第0项为第一年工资
        self.total_salary = 0  # 累积工资
        self.house = house  # 目标房屋

    def get_salary(self) -> list:  # 获得每年工作
        for i in range(1, self.year + 1):
            if i == 1:
                self.salary_per_year.append(self.salary)
            else:
                n = self.salary_per_year[i - 2]
                if n < 60:
                    self.salary_per_year.append(n * 1.15)
                else:
                    self.salary_per_year.append(n * 1.05)
        return self.salary_per_year

    def get_total_salary(self) -> float:  # 总薪资统计
        s = 0
        for value in self.salary_per_year:
            s += value
        self.total_salary = s
        return s

    def get_down_payment(self) -> float:  # 计算首付
        s = self.house.get_price()
        ss = s * (1.1**(self.year-1))
        ss = ss*0.3
        return ss


class apartment:
    def __init__(self, houseprice):
        self.price = houseprice  # 初始房价

    def get_price(self):  # 获得初始房价
        return self.price


if __name__ == '__main__':
    y = 0
    h = apartment(600)
    # 第y年能否买
    for num in range(1, 30):
        p = person(30, num, h)
        price = p.get_salary()
        total_price = p.get_total_salary()
        shoufu = p.get_down_payment()
        if total_price >= shoufu:
            print(f'{num} year can buy!')
            y = num
            break
    # 第y+10年能否买
    y = y + 10
    print(f'at {y} year')
    p2 = person(30, y, h)
    price = p2.get_salary()
    total_price = p2.get_total_salary()
    shoufu = p2.get_down_payment()
    if total_price >= shoufu:
        print(f'{y} year can buy!')
    else:
        print(f'{y} year cant buy!')

