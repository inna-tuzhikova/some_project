from argparse import ArgumentParser

from some_project.utils import double, fib, triple


def main():
    parser = ArgumentParser('Simple test script')
    parser.add_argument(
        'operator',
        type=str, choices=['double', 'triple', 'fib'],
        help='Choose unary operation'
    )
    parser.add_argument(
        'operand',
        type=int,
        help='Operand to chosen operator'
    )

    args = parser.parse_args()
    calc(args.operator, args.operand)


def calc(operator: str, operand: int):
    op_map = dict(
        double=double,
        triple=triple,
        fib=fib
    )
    fun = op_map.get(operator)
    if fun is None:
        raise ValueError(f'Unknown operator: `{operator}`')
    value = fun(operand)
    print(f'{operator}({operand}) = {value}')


if __name__ == '__main__':
    main()
