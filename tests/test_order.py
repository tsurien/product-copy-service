import pytest

from order import calculate_order_total


@pytest.mark.parametrize(
    "item_total, member_grade, expected",
    [
        # 50,000원 미만: 상품 할인 후 배송비 3,000원 추가
        (49_900, "VIP", 42_920),
        (49_900, "GOLD", 45_415),
        (49_900, "SILVER", 47_910),

        # 정확히 50,000원: 배송비 무료
        (50_000, "VIP", 40_000),
        (50_000, "GOLD", 42_500),
        (50_000, "SILVER", 45_000),

        # 50,000원 초과: 배송비 무료
        (60_000, "VIP", 48_000),
        (60_000, "GOLD", 51_000),
        (60_000, "SILVER", 54_000),
    ],
)
def test_calculate_order_total(item_total, member_grade, expected):
    result = calculate_order_total(item_total, member_grade)

    assert result == pytest.approx(expected)


@pytest.mark.parametrize("item_total", [0, -1, -10_000])
@pytest.mark.parametrize("member_grade", ["VIP", "GOLD", "SILVER"])
def test_calculate_order_total_rejects_non_positive_amount(
    item_total, member_grade
):
    with pytest.raises(ValueError):
        calculate_order_total(item_total, member_grade)