testsuite algorithms:
    setup:
        $ _test.transition_timeout = 0.01
        $ _test.timeout = 8.0
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"
        click "开始游戏"
    teardown:
        exit
    testcase all_correct:
        advance until screen "algorithm_question"
        click id "solution_1"
        assert screen "algorithm_feedback"
        assert eval (xi_trust == 70 and inefficient_count == 0)
        click "继续剧情"
        advance until screen "algorithm_question"
        click id "solution_2"
        click "继续剧情"
        advance until screen "algorithm_question"
        click id "solution_3"
        click "继续剧情"
        advance until screen "ending_report"
        assert eval (xi_trust == 90 and inefficient_count == 0 and not bad_end_reason)
        assert eval (solved_01 and solved_02 and solved_03)
        assert eval (len(algorithm_records) == 3)
    testcase three_inferior:
        advance until screen "algorithm_question"
        click id "solution_2"
        assert eval (xi_trust == 40 and inefficient_count == 1 and not bad_end_reason)
        click "继续剧情"
        advance until screen "algorithm_question"
        click id "solution_0"
        assert eval (xi_trust == 20 and inefficient_count == 2 and not bad_end_reason)
        click "继续剧情"
        advance until screen "algorithm_question"
        click id "solution_2"
        assert eval (xi_trust == 0 and inefficient_count == 3 and bool(bad_end_reason))
        click "查看结局"
        advance until screen "ending_report"
        assert eval (len(algorithm_records) == 3)
    testcase wrong_ends_story:
        parameter (question_id, option_index) = [("q01", 0), ("q01", 3), ("q02", 1), ("q02", 3), ("q03", 0), ("q03", 1)]
        run Jump("question_" + question_id[1:])
        pause until screen "algorithm_question"
        click id ("solution_%d" % option_index)
        assert screen "algorithm_feedback"
        assert eval (xi_trust == 0 and bool(bad_end_reason))
        click "查看结局"
        advance until screen "ending_report"
        assert eval (len(algorithm_records) == 1)
    testcase inferior_data:
        $ options = [(qid, i) for qid, q in ALGORITHM_QUESTIONS.items() for i, option in enumerate(q["options"]) if option[1] == "inferior"]
        assert eval (len(options) == 6)
        python:
            for qid, i in options:
                store.xi_trust = 60
                store.inefficient_count = 0
                store.bad_end_reason = ""
                store.algorithm_records = []
                result = apply_algorithm_solution(qid, i)
                assert store.xi_trust == 40 and store.inefficient_count == 1 and not store.bad_end_reason
                assert result["kind"] == "inferior"
            for q in ALGORITHM_QUESTIONS.values():
                assert len(q["options"]) == 5
                assert sorted(o[1] for o in q["options"]) == ["correct", "inferior", "inferior", "wrong", "wrong"]
