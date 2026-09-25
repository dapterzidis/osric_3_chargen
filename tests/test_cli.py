import pytest
import cli
import data


@pytest.fixture
def typed(monkeypatch):
    """Replace input() with a scripted list of answers.

    Usage inside a test:  typed("abc", "3")
    If the code asks for more input than scripted, the test fails
    (StopIteration) instead of hanging forever.
    """
    def _set(*answers):
        answers = iter(answers)
        monkeypatch.setattr("builtins.input", lambda prompt="": next(answers))
    return _set


@pytest.fixture
def fixed_rolls(monkeypatch):
    """Replace chargen.generate_stats so cli tests don't depend on dice.

    Returns a list that records the dice_per_roll argument of every call.
    """
    calls = []

    def fake_generate_stats(dice_per_roll):
        calls.append(dice_per_roll)
        return [18, 17, 16, 15, 14, 13]

    monkeypatch.setattr(cli.chargen, "generate_stats", fake_generate_stats)
    return calls


# ---------------------------------------------------------------- select_ability_generation_method

@pytest.mark.parametrize("choice", ["0", "1", "2", "3", "4"])
def test_select_method_accepts_valid_choice(typed, choice):
    typed(choice)
    assert cli.select_ability_generation_method() == int(choice)


def test_select_method_reprompts_until_valid(typed):
    typed("abc", "", "-1", "5", "2")
    assert cli.select_ability_generation_method() == 2


# ---------------------------------------------------------------- assign_abilities_manually

def test_assign_manually_sets_each_ability_in_order(typed):
    abilities = data.ability_list.copy()
    typed("18", "17", "16", "15", "14", "13")

    cli.assign_abilities_manually(abilities)

    assert abilities == {"STR": 18, "DEX": 17, "CON": 16, "INT": 15, "WIS": 14, "CHA": 13}


def test_assign_manually_rejects_out_of_range(typed, capsys):
    abilities = data.ability_list.copy()
    typed("2", "19", "3", "10", "10", "10", "10", "10")

    cli.assign_abilities_manually(abilities)

    assert abilities["STR"] == 3
    assert capsys.readouterr().out.count("INVALID VALUE") == 2


# ---------------------------------------------------------------- choose_roll_order

def test_choose_roll_order_assigns_picked_rolls(typed):
    abilities = data.ability_list.copy()
    rolls = [9, 12, 15, 8, 10, 14]
    typed("15", "14", "12", "10", "9", "8")

    cli.choose_roll_order(abilities, rolls)

    assert abilities == {"STR": 15, "DEX": 14, "CON": 12, "INT": 10, "WIS": 9, "CHA": 8}
    assert rolls == [9, 12, 15, 8, 10, 14]  # caller's list is left untouched


def test_choose_roll_order_rejects_roll_already_used(typed):
    abilities = data.ability_list.copy()
    typed("15", "15", "12", "11", "10", "9", "8")  # second "15" is no longer available

    cli.choose_roll_order(abilities, [15, 12, 11, 10, 9, 8])

    assert abilities["DEX"] == 12


def test_choose_roll_order_handles_duplicate_rolls(typed):
    abilities = data.ability_list.copy()
    typed("10", "10", "10", "9", "9", "9")

    cli.choose_roll_order(abilities, [10, 10, 10, 9, 9, 9])

    assert sorted(abilities.values()) == [9, 9, 9, 10, 10, 10]


# ---------------------------------------------------------------- generate_ability_scores

@pytest.mark.parametrize("method, dice", [(1, 3), (3, 4)])
def test_in_order_methods_use_rolls_in_order(fixed_rolls, method, dice):
    abilities = cli.generate_ability_scores(method)

    assert list(abilities.values()) == [18, 17, 16, 15, 14, 13]
    assert fixed_rolls == [dice]


@pytest.mark.parametrize("method, dice", [(2, 3), (4, 4)])
def test_pick_order_methods_let_player_arrange(typed, fixed_rolls, method, dice):
    typed("13", "14", "15", "16", "17", "18")

    abilities = cli.generate_ability_scores(method)

    assert list(abilities.values()) == [13, 14, 15, 16, 17, 18]
    assert fixed_rolls == [dice]


def test_method_0_is_manual_entry(typed, fixed_rolls):
    typed("10", "11", "12", "13", "14", "15")

    abilities = cli.generate_ability_scores(0)

    assert list(abilities.values()) == [10, 11, 12, 13, 14, 15]
    assert fixed_rolls == []  # no dice rolled


def test_unknown_method_raises():
    with pytest.raises(Exception):
        cli.generate_ability_scores(99)


def test_generate_does_not_modify_shared_template(fixed_rolls):
    cli.generate_ability_scores(1)
    assert all(v == 0 for v in data.ability_list.values())


# ---------------------------------------------------------------- select_desired_race

def test_select_race_returns_race_at_chosen_index(typed):
    races = sorted(list(data.race_list) + ["any"])
    typed(str(races.index("elf")))
    assert cli.select_desired_race() == "elf"


def test_select_race_can_pick_any(typed):
    races = sorted(list(data.race_list) + ["any"])
    typed(str(races.index("any")))
    assert cli.select_desired_race() == "any"


def test_select_race_reprompts_on_invalid(typed):
    races = sorted(list(data.race_list) + ["any"])
    typed("x", "-1", str(len(races)), "0")
    assert cli.select_desired_race() == races[0]


# ---------------------------------------------------------------- select_desired_class

@pytest.mark.parametrize("race", list(data.race_list))
def test_select_class_menu_lists_race_classes(typed, capsys, race):
    typed("0")
    cli.select_desired_class(race)

    menu = capsys.readouterr().out
    for cls in data.race_list[race]["classes"]:
        assert cls in menu


def test_select_class_hides_classes_race_cannot_take(typed, capsys):
    typed("0")
    cli.select_desired_class("dwarf")

    menu = capsys.readouterr().out
    assert "magic-user" not in menu
    assert "monk" not in menu


def test_select_class_for_any_race_includes_every_class(typed, capsys):
    typed("0")
    cli.select_desired_class("any")

    menu = capsys.readouterr().out
    for race in data.race_list.values():
        for cls in race["classes"]:
            assert cls in menu


def test_select_class_human_cannot_pick_multiclass(typed):
    classes = sorted(data.race_list["human"]["classes"] + ["any"])
    for i in range(len(classes)):
        typed(str(i))
        assert "/" not in cli.select_desired_class("human")