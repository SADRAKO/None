# Replace question data here; the runner, saves and ending rules stay reusable.
init python:
    ALGORITHM_QUESTIONS = {
        "q01": {
            "title": "检修一｜重复的脉冲码",
            "source": "字符串计数 · 参考 Codeforces 977B",
            "text": "B-17 不断发送大写字母日志。找出出现次数最多的连续两个字符；位置允许重叠，并列时任选。日志可长达 100000 个字符。",
            "sample": "日志：ZZZAA\n两字符依次为 ZZ、ZZ、ZA、AA，答案为 ZZ，出现 2 次。",
            "hints": ["每个相邻位置都要检查，不能跳过中间的字符。", "用计数表记录每种两字符脉冲出现了几次。", "遍历 i = 0 到 n-2，给 s[i:i+2] 计数，再取最大值。"],
            "options": [
                ("A. 每次向后跳两格，只统计不重叠的字符对。", "wrong", "ZZZAA 中会漏掉第二个 ZZ。步长应为 1。", "O(n)，但答案错误"),
                ("B. 遍历所有相邻位置，用 26×26 表计数并取最大值。", "correct", "每个起点只处理一次，重叠位置也计入。固定字符集只需 676 个计数格。", "时间 O(n)，额外空间 O(1)"),
                ("C. 对每个位置，重新扫描整条日志计算该字符对的次数。", "inferior", "可以得到正确结果，但 n 个候选各扫描 n 次。十万字符约需百亿次比较，检修窗口无法承受。", "时间 O(n²)，额外空间 O(1)"),
                ("D. 把字符对放进集合，输出字典序最小的一对。", "wrong", "集合丢掉了次数，字典序也不能说明哪个脉冲最频繁。", "遗漏频次信息"),
                ("E. 为每一个相邻位置复制整条日志，再逐个计数。", "inferior", "复制与统计可保留正确结果，但为每个起点保存全量日志浪费大量内存和时间。", "时间 O(n²)，额外空间 O(n²)")],
            "reference": "遍历所有相邻位置，用固定大小的二维计数表统计频次。"
        },
        "q02": {
            "title": "检修二｜重试队列去重",
            "source": "哈希集合 · 交接日志场景练习",
            "text": "旧终端重复提交交接记录。保留每个日志编号第一次出现的那一行，并保持原顺序。编号没有大小写差异。队列最多包含 100000 条记录。",
            "sample": "输入：BELL/04、D17、BELL/04、C02、D17\n保留：BELL/04、D17、C02",
            "hints": ["已经保留过的编号，之后都应跳过。", "集合适合快速判断编号有没有出现过。", "按原队列顺序遍历：不在集合就加入集合并输出，否则跳过。"],
            "options": [
                ("A. 每读一条记录，就线性扫描所有已保留的记录。", "inferior", "保持顺序且答案正确，但全是不重复记录时需比较 1+2+…+(n-1) 次。", "时间 O(n²)，空间 O(n)"),
                ("B. 只比较当前记录与紧邻的上一条，相同就跳过。", "wrong", "重复记录可能不相邻。BELL/04 与 D17 在样例中都会再次被保留。", "不能处理不相邻重复"),
                ("C. 用集合记录已见编号，首次出现就按原顺序保留。", "correct", "集合负责查重，输出列表负责顺序。两种职责分开，既正确又高效。", "平均时间 O(n)，空间 O(n)"),
                ("D. 每次遇到重复编号，就删掉第一次出现的那一行。", "wrong", "题目要求保留第一次出现。删除首行会破坏输出位置与交接顺序。", "保留规则错误"),
                ("E. 每次插入记录前，把已见编号重新排序后再二分查找。", "inferior", "查重正确，也能另存原输出顺序，但反复排序比一次集合查找贵得多。", "时间 O(n² log n)，空间 O(n)")],
            "reference": "顺序扫描队列，用哈希集合查重，用列表保留首现顺序。"
        },
        "q03": {
            "title": "检修三｜负载预算",
            "source": "排序与贪心 · 参考 Codeforces 1185C1",
            "text": "对每个位置 i，必须保留当前测试 a[i]，只允许跳过此前的测试。求让已保留测试总耗时不超过 M 所需的最少跳过次数。耗时为正且每项不超过 M；本次最多 100 项。",
            "sample": "M = 15，耗时：1 2 3 4 5 6 7\n答案：0 0 0 0 0 2 3\n第 6 项保留 6，跳过 5、4 后耗时为 12；第 7 项保留 7，跳过 6、5、4 后耗时为 13。", 
            "hints": ["每个位置单独计算，当前项不能删。", "要删除的项数最少，一次应尽量减少更多耗时。", "把此前测试从大到小排序，逐项扣除，直到总和不超过预算。"],
            "options": [
                ("A. 从最早的测试开始跳过，直到总耗时不超预算。", "wrong", "最早不代表耗时最大。M=10，前项 1、9，当前项 2：删 9 一次即可，按时间顺序却删两次。", "不能保证最少次数"),
                ("B. 当前项最大时先跳过当前项，省下更多预算。", "wrong", "当前测试必须保留，跳过它违反约束。", "违反保留当前项的约束"),
                ("C. 枚举此前测试的所有子集，挑出最少的可行删除集合。", "inferior", "能找到最优答案，但 100 个测试的子集数量约为 2 的 100 次方，无法在窗口内完成。", "指数时间 O(n·2^n)"),
                ("D. 对每个位置排序此前耗时，从大到小跳过直到达标。", "correct", "删除 k 个测试时，最大的 k 个带来最多节省；更少的项若还不够，就不存在更少的可行方案。本次小规模可直接排序。", "总时间 O(n² log n)，空间 O(n)"),
                ("E. 枚举此前测试的所有删除顺序，取最少删除数。", "inferior", "答案可以正确，但同一删除集合被不同顺序反复计算，工作量比枚举子集更大。", "阶乘级时间 O(n·n!)")],
            "reference": "固定当前测试，对此前耗时降序排列，优先跳过最大项。"
        }
    }

    def apply_algorithm_solution(question_id, option_index):
        question = ALGORITHM_QUESTIONS[question_id]
        caption, kind, explanation, cost = question["options"][option_index]
        if kind == "correct":
            store.xi_trust = min(100, store.xi_trust + 10)
        elif kind == "inferior":
            store.inefficient_count += 1
            store.xi_trust = max(0, store.xi_trust - 20)
        else:
            store.xi_trust = 0
            store.bad_end_reason = "错误解法使检修判断失效。"
        if store.inefficient_count >= 3:
            store.bad_end_reason = "三次低效方案耗尽了交接窗口。"
        record = {"question_id": question_id, "title": question["title"], "caption": caption,
                  "kind": kind, "explanation": explanation, "cost": cost,
                  "trust": store.xi_trust, "inferior_count": store.inefficient_count}
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
            call screen algorithm_feedback(solution_record, ALGORITHM_QUESTIONS[question_id])
            if bad_end_reason:
                $ current_question_id = None
                jump bad_end
            $ setattr(store, "solved_" + question_id[1:], True)
            $ current_question_id = None
            return
