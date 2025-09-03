# Algovid

A comprehensive group theory application with a REST API backend, Swift CLI frontend, and mathematical validation utilities.

## 🏗️ Project Structure

```
Algovid/
├── backend/                 # Express.js REST API server
│   ├── index.js            # Main server with MongoDB integration
│   ├── package.json        # Node.js dependencies
│   └── package-lock.json   # Dependency lock file
├── frontend/               # Swift CLI application
│   └── Sources/
│       └── Algovid/
│           └── main.swift  # Interactive CLI for group management
├── math/                   # Python mathematical utilities
│   └── group_utils.py     # Group theory validation functions
└── shared/                 # Shared resources (empty)
```

## 🚀 Backend (Express.js + MongoDB)

### Overview
A RESTful API server built with Express.js that manages group data in MongoDB.

### Features
- **MongoDB Integration**: Stores group data with Mongoose ODM
- **CORS Support**: Cross-origin requests enabled
- **JSON API**: RESTful endpoints for group management
- **Error Handling**: Comprehensive error responses
- **Validation**: Input validation for required fields

### API Endpoints

#### GET `/api/groups`
Returns all group documents from MongoDB.

**Response:**
```json
[
  {
    "_id": "507f1f77bcf86cd799439011",
    "name": "Cyclic Group C3",
    "description": "A cyclic group of order 3",
    "structure": {
      "type": "multiplication_table",
      "table": {
        "e": {"e": "e", "a": "a", "b": "b"},
        "a": {"e": "a", "a": "b", "b": "e"},
        "b": {"e": "b", "a": "e", "b": "a"}
      }
    }
  }
]
```

#### POST `/api/groups`
Creates a new group document.

**Request Body:**
```json
{
  "name": "Group Name",
  "description": "Group description",
  "structure": {
    "type": "multiplication_table",
    "table": {...}
  }
}
```

**Response:** Created group object with MongoDB `_id`

### Database Schema
```javascript
{
  name: String (required),
  description: String (default: ''),
  structure: Object (default: {})
}
```

### Running the Backend
```bash
cd backend
npm install
node index.js
```

Server runs on `http://localhost:4000`

## 🖥️ Frontend (Swift CLI)

### Overview
An interactive command-line interface built in Swift for managing groups through the REST API.

### Features
- **Async/Await**: Modern Swift concurrency
- **HTTP Client**: URLSession-based API communication
- **JSON Handling**: Custom Codable implementation for complex types
- **Interactive CLI**: Menu-driven user interface
- **Error Handling**: User-friendly error messages

### CLI Options
1. **List all groups** - Fetches and displays groups from backend
2. **Add new group** - Interactive form to create groups
3. **Exit** - Quit the application

### Group Model
```swift
struct Group: Codable {
    let id: String?
    let name: String
    let description: String
    let structure: [String: Any]
}
```

### Running the Frontend
```bash
cd frontend
swift run
```

## 🧮 Math Utilities (Python)

### Overview
Python utilities for validating group theory structures and checking mathematical properties.

### Functions

#### `is_valid_group(structure: dict) -> bool`
Validates if a multiplication table satisfies the basic group axioms:

1. **Closure**: Every product in the table is in the set of elements
2. **Associativity**: `(a * b) * c == a * (b * c)` for all a, b, c
3. **Identity**: Exists element e where `e * a == a * e == a` for all a
4. **Inverses**: For every element a, exists b where `a * b == b * a == e`

#### `find_identity(structure: dict) -> str`
Finds the identity element in a group multiplication table.

#### `find_inverse(structure: dict, element: str) -> str`
Finds the inverse of a specific element in the group.

#### `get_group_elements(structure: dict) -> Set[str]`
Extracts the set of group elements from a multiplication table.

### Example Usage
```python
from math.group_utils import is_valid_group

# Valid cyclic group of order 3
table = {
    'e': {'e': 'e', 'a': 'a', 'b': 'b'},
    'a': {'e': 'a', 'a': 'b', 'b': 'e'},
    'b': {'e': 'b', 'a': 'e', 'b': 'a'}
}

print(is_valid_group(table))  # True
```

## 🔧 Technology Stack

### Backend
- **Node.js** - JavaScript runtime
- **Express.js** - Web framework
- **MongoDB** - NoSQL database
- **Mongoose** - MongoDB ODM
- **CORS** - Cross-origin resource sharing

### Frontend
- **Swift** - Programming language
- **Foundation** - Core framework
- **URLSession** - HTTP networking
- **Codable** - JSON serialization

### Math Utilities
- **Python** - Programming language
- **Type hints** - Static type checking
- **Standard library** - No external dependencies

## 🚀 Getting Started

### Prerequisites
- Node.js (v14+)
- MongoDB (running on localhost:27017)
- Swift (v5.5+)
- Python (v3.7+)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Algovid
   ```

2. **Start MongoDB**
   ```bash
   # Make sure MongoDB is running on localhost:27017
   ```

3. **Start the backend**
   ```bash
   cd backend
   npm install
   node index.js
   ```

4. **Run the frontend**
   ```bash
   cd frontend
   swift run
   ```

5. **Test math utilities**
   ```bash
   cd math
   python -c "from group_utils import is_valid_group; print('Math utilities ready!')"
   ```

## 📝 Usage Examples

### Creating a Group via CLI
```
=== Group Management CLI ===

Options:
1. List all groups
2. Add new group
3. Exit
Enter your choice (1-3): 2

=== Add New Group ===
Enter group name: Cyclic Group C3
Enter group description (optional): A cyclic group of order 3
Enter structure as JSON (optional, press Enter to skip): {"type": "multiplication_table", "table": {"e": {"e": "e", "a": "a", "b": "b"}, "a": {"e": "a", "a": "b", "b": "e"}, "b": {"e": "b", "a": "e", "b": "a"}}}

Creating group...
✅ Group created successfully!
   Name: Cyclic Group C3
   Description: A cyclic group of order 3
   ID: 507f1f77bcf86cd799439011
```

### Validating Groups with Python
```python
from math.group_utils import is_valid_group, find_identity, find_inverse

# Define a group multiplication table
group_table = {
    'e': {'e': 'e', 'a': 'a', 'b': 'b'},
    'a': {'e': 'a', 'a': 'b', 'b': 'e'},
    'b': {'e': 'b', 'a': 'e', 'b': 'a'}
}

# Validate the group
if is_valid_group(group_table):
    print("✅ Valid group!")
    print(f"Identity: {find_identity(group_table)}")
    print(f"Inverse of 'a': {find_inverse(group_table, 'a')}")
else:
    print("❌ Not a valid group")
```

## 🧪 Testing

### Backend API Testing
```bash
# Test GET endpoint
curl http://localhost:4000/api/groups

# Test POST endpoint
curl -X POST http://localhost:4000/api/groups \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Group", "description": "Test", "structure": {}}'
```

### Math Utilities Testing
```python
# Test with known valid groups
python -c "
from math.group_utils import is_valid_group
table = {'e': {'e': 'e', 'a': 'a'}, 'a': {'e': 'a', 'a': 'e'}}
print('Valid group:', is_valid_group(table))
"
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the ISC License.

## 🎯 Future Enhancements

- [ ] Web-based UI for group visualization
- [ ] Advanced group theory algorithms
- [ ] Group isomorphism detection
- [ ] Subgroup and normal subgroup analysis
- [ ] Group presentation support
- [ ] Integration with mathematical software (Sage, GAP) 