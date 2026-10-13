init python:
    ALGORITHM_QUESTIONS = {
        "q01": {
            "title": "题目 1｜找零 · 贪心算法",
            "source": "C 语言填空｜面额 50、20、10、5、1，change(63) 返回 5",
            "text": "补全 change 函数：每轮用当前面额尽可能多地找零，再把剩余金额交给下一档。",
            "sample": "count += ______；amount = ______；\n63：拿 1 张 50，剩 13；拿 1 张 10，剩 3；拿 3 张 1。",
            "hints": ["别一张一张拿。当前面额能拿几张，直接用除法。", "拿完一档之后，手里还剩多少没找？", "两个空分别是商 amount / coins[i]，以及余数 amount % coins[i]。"],
            "options": [
                ("A. count += amount / coins[i]；amount = amount % coins[i]。", "correct", "商表示这一档拿几张，余数表示拿完后的剩余金额。", "时间 O(面额种类)，空间 O(1)"),
                ("B. count += amount % coins[i]；amount = amount / coins[i]。", "wrong", "这是在数\"还剩多少\"，不是\"拿了几张\"。你想想 63 除以 50，你要的是商还是余数？", "变量含义错位"),
                ("C. count += amount / coins[i]；amount = amount。", "wrong", "你把 63 拿去除了五次，每次都是整整 63。每拿完一档，剩下的钱应该变少啊。", "状态没有更新"),
                ("D. count += coins[i] / amount；amount = coins[i] % amount。", "wrong", "除法方向反了。应该用待找金额除以面额，而不是面额除以待找金额。", "除法方向错误"),
                ("E. 每次 amount -= 1，直到 amount 为 0，再统计减了多少次。", "wrong", "这样数出来的是 63 枚，不是 5 张——整个过程完全没有用到面额。", "答案错误")],
            "reference": "商负责计数，余数负责更新状态；标准面额体系下使用贪心。"
        },
        "q02": {
            "title": "题目 2｜窄书架 · 冒泡排序",
            "source": "相邻交换｜数组 5、2、4、1、3｜交换次数为 7",
            "text": "只能交换相邻两本书。补全冒泡排序的循环边界和比较条件，并判断样例一共交换几次。",
            "sample": "for (j = 0; j < ______; j++)\n    if (______ ) swap(a[j], a[j+1]);\n样例交换次数：7。",
            "hints": ["每次只比较相邻元素，j 不能让 j+1 走到数组外。", "每一趟结束，最右侧未排序区域的最大值已经到位。", "条件是 j < n - 1 - i，比较是 a[j] > a[j + 1]。"],
            "options": [
                ("A. j < n；if (a[j] > a[j+1])。", "wrong", "j 到 n-1 时会访问 a[n]，数组越界；边界必须给 j+1 留位置。", "存在越界访问"),
                ("B. j < n - 1 - i；if (a[j] > a[j+1])。", "correct", "相邻比较时大的元素向右冒泡；每趟最后一个位置已经有序。样例交换 7 次。", "时间 O(n²)，空间 O(1)"),
                ("C. j < n - 1；if (a[j] < a[j+1])。", "wrong", "比较方向会把较小值推到右侧，得到降序结果，不符合从小到大排序。", "排序方向错误"),
                ("D. 每趟都 j < n - 1，不缩短范围。", "inferior", "能跑。可是每趟结束后，最右边已经是排好的了，后面那些比较全是白做。", "时间仍为 O(n²)，常数更大"),
                ("E. 每次找到最小值，和当前位置交换一次。", "inferior", "这是选择排序的思路，不满足本题只能相邻交换的限制；若逐格移动还会增加交换次数。", "不符合操作限制")],
            "reference": "相邻比较，大的向右沉；每趟缩短未排序区间。"
        },
        "q03": {
            "title": "题目 3｜猜数字 · 二分查找",
            "source": "有序数组｜边界更新｜复杂度 O(log n)",
            "text": "补全有序数组中的二分查找。找到 target 返回下标，找不到返回 -1。",
            "sample": "mid = ______；a[mid] < target 时 l = ______；否则 r = ______。\n每次排除一半范围。",
            "hints": ["中间位置是左右端点的平均值；减法写法还能避免整数溢出。", "mid 处已经小于 target，mid 自己不可能是答案，左边界要越过它。", "三个空分别是 l + (r-l)/2、mid+1、mid-1。"],
            "options": [
                ("A. mid=(l+r)/2；l=mid；r=mid。", "wrong", "这样 mid 自己还留在范围里。如果剩下两个元素，l = mid 会一直原地踏步，程序永远退不出去。", "边界不收缩"),
                ("B. mid=l+(r-l)/2；l=mid+1；r=mid-1。", "correct", "中点安全，且排除已经比较过的 mid；复杂度为 O(log n)。", "时间 O(log n)，空间 O(1)"),
                ("C. 从 l 到 r 逐个比较，遇到 target 就返回。", "inferior", "结果正确，但没有利用有序性；最坏要比较 n 个元素。", "时间 O(n)"),
                ("D. mid=(l+r)/2；a[mid]<target 时 r=mid-1，否则 l=mid+1。", "wrong", "左右更新方向反了，target 在右边时却缩掉了正确答案。", "区间方向错误"),
                ("E. 每次重新排序 a，再从头线性查找。", "inferior", "查找结果可能正确，但每次排序都破坏了效率，远差于直接利用已有顺序。", "至少 O(n log n) 每轮")],
            "reference": "前提是有序；比较中点后排除半边，并用 mid±1 收缩边界。"
        },
        "q04": {
            "title": "题目 4｜天台楼梯 · 递归",
            "source": "终止条件 + 拆分｜climb(10) = 89",
            "text": "一次走一级或两级。补全递归函数，使 climb(1)=1、climb(2)=2，并计算 climb(10)。",
            "sample": "if (________) return n;\nreturn ________;\nclimb(10) 的答案：89。",
            "hints": ["递归必须有终止条件，最小的两种台阶情况已经算出来了。", "站在 n 级，最后一步来自 n-1 或 n-2。", "两个空是 n <= 2，以及 climb(n-1) + climb(n-2)。"],
            "options": [
                ("A. if (n == 0) return 1；return climb(n-1) + climb(n-2)。", "wrong", "终止条件只覆盖 n == 0。climb(1) 会去算 climb(-1)、climb(-2)……一路减下去，永远回不来，直接栈溢出。", "无限递归"),
                ("B. if (n <= 2) return n；return climb(n-1) + climb(n-2)。", "correct", "终止条件覆盖 1、2 级，拆分对应最后一步来自 n-1 或 n-2，climb(10)=89。", "直接递归时间指数级，空间 O(n)"),
                ("C. if (n <= 2) return n；return climb(n-1) * climb(n-2)。", "wrong", "两类走法是相加，不是相乘；乘法会把不相同的路径组合错误。", "递推关系错误"),
                ("D. if (n <= 2) return n；return climb(n-1)。", "wrong", "只考虑迈一级，漏掉迈两级的所有走法。", "漏解"),
                ("E. 用循环从 1 数到 n，每次暴力枚举所有走法。", "inferior", "可以通过枚举得到结果，但会重复探索大量相同子问题；用记忆化或 DP 更好。", "重复计算严重")],
            "reference": "递归由终止条件和同类子问题拆分组成；斐波那契式结果可用 DP 优化。"
        },
        "q05": {
            "title": "题目 5｜代币兑换 · 动态规划",
            "source": "重叠子问题｜面额 1、5、11｜min_coins(15) = 3",
            "text": "用 dp[i] 表示凑出 i 点最少需要的代币数。补全转移，并判断 min_coins(15)。",
            "sample": "if (i >= coins[j] && ______ < dp[i])\n    dp[i] = ______;\ndp[10]=2，dp[4]=4，dp[14]=4。",
            "hints": ["最后一个代币是 coins[j] 时，前面还要凑 i - coins[j]。", "前面的答案已经写在 dp[i-coins[j]] 里，加上最后这个代币就是 +1。", "两个空是同一个表达式：dp[i - coins[j]] + 1。"],
            "options": [
                ("A. 比较并赋值 dp[i - coins[j]] + 1；min_coins(i) + 1。", "wrong", "第二个空写成了 min_coins(i) + 1，而它就在 min_coins(i) 自己里面，会无限递归、永远返回不了。转移要用已经算好的 dp 数组。", "写成了自我递归"),
                ("B. 比较并赋值 dp[i - 1] + 1；min_coins(15) 返回 3。", "wrong", "这是只拿面额 1 的情况。5 和 11 呢？你要对每个面额都试一遍。", "漏掉其他状态转移"),
                ("C. 比较并赋值 dp[i - coins[j]] + 1；min_coins(15) 返回 3。", "correct", "尝试每种最后代币，取最小转移；dp[10]+1=3，得到 5+5+5。", "时间 O(target×面额种类)，空间 O(target)"),
                ("D. 比较并赋值 dp[i - coins[j]]；min_coins(15) 返回 3。", "wrong", "忘了把刚拿的这个代币计入数量。少了 +1，dp 会一路塌下去：dp[5] 直接从 dp[0] 得到 0，最后 min_coins(15) 返回 0，而不是少一个。", "漏加 1"),
                ("E. 每个金额都从头枚举所有代币组合，再挑最少的。", "inferior", "可以得到正确答案，但会反复计算同一个金额；动态规划用表避免重复。", "组合枚举会呈指数增长")],
            "reference": "从小到大计算 dp，转移为 min(dp[i-coins[j]]+1)，避免重复计算。"
        }
    }

    def apply_algorithm_solution(question_id, option_index):
        question = ALGORITHM_QUESTIONS[question_id]
        caption, kind, explanation, cost = question["options"][option_index]
        if kind == "correct":
            store.c_trust = min(100, store.c_trust + 8)
        elif kind == "inferior":
            store.inefficient_count += 1
            store.c_trust = max(0, store.c_trust - 20)
        else:
            store.c_trust = 0
            store.bad_end_reason = "错误解法让 C 失去了继续交给你的信心。"
        if store.inefficient_count >= 3:
            store.bad_end_reason = "三次低效方案让补习时间全部耗尽。"
        record = {"question_id": question_id, "title": question["title"], "caption": caption, "kind": kind,
                  "explanation": explanation, "cost": cost, "trust": store.c_trust,
                  "inferior_count": store.inefficient_count}
        store.algorithm_records.append(record)
        return record

label run_algorithm_question(question_id):
    $ current_question_id = question_id
    $ hint_stage = 0
    while True:
        call screen algorithm_question(ALGORITHM_QUESTIONS[question_id])
        $ selected_solution = _return
        if selected_solution == "hint":
            $ hint_stage = min(3, hint_stage + 1)
        else:
            $ solution_record = apply_algorithm_solution(question_id, selected_solution)
            if solution_record["kind"] == "correct":
                play sound "audio/sfx/correct.ogg"
            elif solution_record["kind"] == "inferior":
                play sound "audio/sfx/inferior.ogg"
            else:
                play sound "audio/sfx/wrong.ogg"
            call screen algorithm_feedback(solution_record, ALGORITHM_QUESTIONS[question_id])
            if bad_end_reason:
                $ current_question_id = None
                jump bad_end
            $ setattr(store, "solved_" + question_id[1:], True)
            $ current_question_id = None
            return

label question_01:
    call run_algorithm_question("q01")
    return
label question_02:
    call run_algorithm_question("q02")
    return
label question_03:
    call run_algorithm_question("q03")
    return
label question_04:
    call run_algorithm_question("q04")
    return
label question_05:
    call run_algorithm_question("q05")
    return
