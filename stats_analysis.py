import argparse
import statistics


def load_numbers(file_path):
    try:
        with open(file_path, 'r') as f:
            contents = f.read()
    except FileNotFoundError:
        raise SystemExit(f"File not found: {file_path}")

    # Split by comma or whitespace
    numbers = []
    for token in contents.replace(',', ' ').split():
        try:
            numbers.append(float(token))
        except ValueError:
            raise ValueError(f"Invalid number found in dataset: {token}")
    if not numbers:
        raise ValueError("No numbers found in dataset")
    return numbers


def compute_statistics(numbers):
    stats = {
        'count': len(numbers),
        'mean': statistics.mean(numbers),
        'median': statistics.median(numbers),
        'variance': statistics.variance(numbers) if len(numbers) > 1 else 0.0,
        'stdev': statistics.stdev(numbers) if len(numbers) > 1 else 0.0,
        'min': min(numbers),
        'max': max(numbers),
    }
    try:
        stats['mode'] = statistics.mode(numbers)
    except statistics.StatisticsError:
        stats['mode'] = None
    return stats


def main():
    parser = argparse.ArgumentParser(description="Compute basic statistics for a dataset")
    parser.add_argument('file', help='Path to file containing numbers')
    args = parser.parse_args()

    numbers = load_numbers(args.file)
    stats = compute_statistics(numbers)

    for k, v in stats.items():
        print(f"{k}: {v}")


if __name__ == '__main__':
    main()
