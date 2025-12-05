# Algovid

Group theory app with a Node.js backend and Python CLI.

A group is a set G with a binary operation (like multiplication) that satisfies four axioms:
- **Closure**: For any a, b in G, the product a * b is also in G
- **Associativity**: (a * b) * c = a * (b * c) for all a, b, c in G
- **Identity**: There exists an element e in G such that e * a = a * e = a for all a in G
- **Inverses**: For every element a in G, there exists an element b in G such that a * b = b * a = e

This app lets you store groups defined by their multiplication tables and automatically validates that they satisfy these axioms.

## Setup

Make sure MongoDB is running on localhost:27017.

Start the backend:
```bash
cd backend
npm install
node index.js
```

Run the CLI:
```bash
cd frontend
python enhanced_cli.py
```

## What it does

- Store groups in MongoDB (name, description, multiplication table)
- Validate groups using group theory axioms
- CLI to add/list/validate groups

## API

- `GET /api/groups` - list all groups
- `POST /api/groups` - create a group

## Math utilities

The `math/group_utils.py` file has functions to check if a multiplication table is a valid group:
- `is_valid_group(table)` - checks closure, associativity, identity, inverses
- `find_identity(table)` - finds the identity element
- `find_inverse(table, element)` - finds an element's inverse
- `get_group_elements(table)` - gets all elements from the table



© 2025 Lyric Hagen. All rights reserved. 
This project was created by Lyric Hagen. Do not present or distribute as your own work.
