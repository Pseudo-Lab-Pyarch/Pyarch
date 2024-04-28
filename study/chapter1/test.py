from datetime import date
from dataclasses import dataclass
from typing import Optional, List
import pytest


@dataclass(frozen=True)
class OrderLine:
    orderid: str
    sku: str
    qty: int


class Batch:
    def __init__(self, ref: str, sku: str, qty: int, eta: Optional[date]):
        # 배치를 식별하는 고유 참조 번호
        self.reference = ref
        # 재고 유지 단위
        self.sku = sku
        # 도착 예정 시간
        self.eta = eta
        # 해당 배치에서 사용할 수 있는 상품의 수량
        self.available_quantity = qty

    def allocate(self, line: OrderLine):
        self.available_quantity -= line.qty

    # 할당을 할 수 있으려면, 배치에 있는 sku과 OrderLine의 sku와 같으면서, available_quantity가 라인에 들어온 수보다 크거나 같아야 한다.
    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.qty

# Batch는 allocate가 일어날 때마다,
# OrderLine의 qty만큼 available_quantity를 감소시키는 코드를 테스트 코드로 만들면 다음과 같다.
def test_allocating_to_a_batch_reduces_the_available_quantity():
    batch = Batch("batch-001", "SMALL-TABLE", qty=20, eta=date.today())
    line = OrderLine("order-ref", "SMALL-TABLE", 2)

    batch.allocate(line)

    assert batch.available_quantity == 18

# 아래의 테스트의 경우, 단순히 available_quantity를 증가시키거나 감소시켜서 구현 가능
def make_batch_and_line(sku, batch_qty, line_qty):
    return (
        Batch("batch-001", sku, batch_qty, eta=date.today()),
        OrderLine("order-123", sku, line_qty),
    )

# 배치 20, 라인 2
def test_can_allocate_if_available_greater_than_required():
    large_batch, small_line = make_batch_and_line("ELEGANT-LAMP", 20, 2)
    assert large_batch.can_allocate(small_line)

# 배치 2, 라인 20
def test_cannot_allocate_if_available_smaller_than_required():
    small_batch, large_line = make_batch_and_line("ELEGANT-LAMP", 2, 20)
    assert small_batch.can_allocate(large_line) is False

# 배치 2, 라인 2
def test_can_allocate_if_available_equal_to_required():
    batch, line = make_batch_and_line("ELEGANT-LAMP", 2, 2)
    assert batch.can_allocate(line)

# sku가 다른 경우
def test_cannot_allocate_if_skus_do_not_match():
    batch = Batch("batch-001", "UNCOMFORTABLE-CHAIR", 100, eta=None)
    different_sku_line = OrderLine("order-123", "EXPENSIVE-TOASTER", 10)
    assert batch.can_allocate(different_sku_line) is False


class Batch:
    def __init__(self, ref: str, sku: str, qty: int, eta: Optional[date]):
        self.reference = ref
        self.sku = sku
        self.eta = eta
        # 내부에서만 변경되므로, private
        self._purchased_quantity = qty
        self._allocations = set()  # type: Set[OrderLine]

    def allocate(self, line: OrderLine):
        if self.can_allocate(line):
            self._allocations.add(line)

    def deallocate(self, line: OrderLine):
        if line in self._allocations:
            self._allocations.remove(line)

    @property
    def allocated_quantity(self) -> int:
        return sum(line.qty for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.qty

# 아래의 경우, 라인에 할당되지 않은 배치를 해제하면 배치의 가용 수량에 영향을 주지 않아야 한다.
def test_can_only_deallocate_allocated_lines():
    batch, unallocated_line = make_batch_and_line("DECORATIVE-TRINKET", 20, 2)
    batch.deallocate(unallocated_line)
    # @property를 이용해서 클래스의 메서드를 괄호를 사용하지 않고 인스턴스 변수로 활용
    assert batch.available_quantity == 20

# 위와 같이 set으로 관리를 하니, 멱동성 테스트(여러번 실행하는 경우)에도 문제가 없음
def test_allocation_is_idempotent():
    batch, line = make_batch_and_line("ANGULAR-DESK", 20, 2)
    batch.allocate(line)
    batch.allocate(line)
    assert batch.available_quantity == 18


# 데이터 클래스
@dataclass(frozen=True)
class OrderLine:
    orderid: str
    sku: str
    qty: int


# 현재 예시에서 배치가 엔티티임 → 라인을 배치에 할당할 수 있고, 배치 도착 예정 날짜를 변경할 수도 있지만,
# 이런 값을 바꿔도 배치는 여전히 정체성이 같은 배치
class Batch:
    def __eq__(self, other):
        if not isinstance(other, Batch):
            return False
        # 다른 객체의 reference 속성이 현재 객체의 reference 속성과 동일한지 확인하는 것을 의미
        return other.reference == self.reference
    # __hash__ 메서드는 객체를 해시 가능(hashable)하게 만듬
    def __hash__(self):
        return hash(self.reference)

#  @dataclass(frozen=True)와 같은 데코레이터를 사용해도, immutable 하도록 만들 수 있음.
@dataclass(frozen=False)
class ImmutableClass:
    x: int
    y: int


# 배치를 표현하는 모델을 만들었지만, 실제로는 모든 재고를 표현하고 구체적인 배치 집합에서 주문 라인을 할당할 수 있어야 함.
# 이런 함수를 테스트 하는 방법은 다음과 같음
def test_prefers_current_stock_batches_to_shipments():
    # 현재 재고가 있는 배치(in_stock_batch)와 배송 중인 배치(shipment_batch)
    in_stock_batch = Batch("in-stock-batch", "RETRO-CLOCK", 100, eta=None)
    shipment_batch = Batch("shipment-batch", "RETRO-CLOCK", 100, eta=tomorrow)
    line = OrderLine("oref", "RETRO-CLOCK", 10)

    # 현재 재고가 있는 배치를 배송 중인 배치보다 선호하여 주문 라인을 할당하는지 확인
    # 즉시 출하가 가능한 재고를 선호하는 할당 로직을 검증

    allocate(line, [in_stock_batch, shipment_batch])

    assert in_stock_batch.available_quantity == 90
    assert shipment_batch.available_quantity == 100

# 여러 배치가 동일한 상품에 대해 다른 도착 예정일(eta)을 가지고 있을 때,
# allocate 함수가 가장 이른 도착 예정일을 가진 배치에 주문 라인을 할당하는지를 확인
def test_prefers_earlier_batches():
    earliest = Batch("speedy-batch", "MINIMALIST-SPOON", 100, eta=today)
    medium = Batch("normal-batch", "MINIMALIST-SPOON", 100, eta=tomorrow)
    latest = Batch("slow-batch", "MINIMALIST-SPOON", 100, eta=later)
    line = OrderLine("order1", "MINIMALIST-SPOON", 10)

    allocate(line, [medium, earliest, latest])

    assert earliest.available_quantity == 90
    assert medium.available_quantity == 100
    assert latest.available_quantity == 100

# 주문 라인을 어떤 배치에 할당했는지를 나타내는 배치 참조 번호를 올바르게 반환하는지 확인
def test_returns_allocated_batch_ref():
    in_stock_batch = Batch("in-stock-batch-ref", "HIGHBROW-POSTER", 100, eta=None)
    shipment_batch = Batch("shipment-batch-ref", "HIGHBROW-POSTER", 100, eta=tomorrow)
    line = OrderLine("oref", "HIGHBROW-POSTER", 10)
    allocation = allocate(line, [in_stock_batch, shipment_batch])
    assert allocation == in_stock_batch.reference


# 서비스
def allocate(line: OrderLine, batches: List[Batch]) -> str:
    batch = next(b for b in sorted(batches) if b.can_allocate(line))
    batch.allocate(line)
    return batch.reference

# 파이썬 마법 메서드 사용 시 모델과 파이썬 숙어 함께 사용 가능
# sorted()가 작동하게 하려면 '__gt__'를 도메인 모델이 구현해야 함
# eta가 None인 배치(즉, 이미 재고에 있는 배치)는 다른 모든 배치보다 우선
# 그 외의 경우, 도착 예정일이 빠른 배치가 우선
class Batch:
    def __gt__(self, other):
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta


# 예외를 사용해 도메인 개념 표현 가능
# 예외로 도메인 개념을 표현하는 것 → 품절로 주문을 할당할 수 없는 개념을 도메인 예외를 사용해 찾아낼 수 있음

# 품절 예외 테스트
def test_raises_out_of_stock_exception_if_cannot_allocate():
    batch = Batch("batch1", "SMALL-FORK", 10, eta=today)
    allocate(OrderLine("order1", "SMALL-FORK", 10), [batch])

    with pytest.raises(OutOfStock, match="SMALL-FORK"):
        allocate(OrderLine("order2", "SMALL-FORK", 1), [batch])

# 도메인 예외 발생
class OutOfStock(Exception):
    pass

def allocate(line: OrderLine, batches: List[Batch]) -> str:
    try:
        batch = next(b for b in sorted(batches) if b.can_allocate(line))
        batch.allocate(line)
        return batch.reference
    except StopIteration:
        raise OutOfStock(f"Out of stock for sku {line.sku}")