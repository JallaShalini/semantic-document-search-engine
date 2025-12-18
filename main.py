import sys
from src.indexer import build_index
from src.search import search, batch_search

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python main.py index")
        print("  python main.py search \"your query\"")
        print("  python main.py batch data/sample_queries.txt")
        return

    command = sys.argv[1]

    if command == "index":
        build_index()

    elif command == "search":
        query = sys.argv[2]
        results = search(query)
        for r in results:
            print(r)

    elif command == "batch":
        query_file = sys.argv[2]
        results = batch_search(query_file)
        for q, res in results.items():
            print(f"\nQuery: {q}")
            for r in res:
                print(r)

    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
