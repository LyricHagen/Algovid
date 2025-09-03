const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 4000;

// Middleware
app.use(cors());
app.use(express.json());

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/algovid', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Group Schema
const groupSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true
  },
  description: {
    type: String,
    default: ''
  },
  structure: {
    type: Object,
    default: {}
  }
});

const Group = mongoose.model('Group', groupSchema);

// Routes

// GET /api/groups - returns all group documents from MongoDB
app.get('/api/groups', async (req, res) => {
  try {
    const groups = await Group.find({});
    res.json(groups);
  } catch (error) {
    console.error('Error fetching groups:', error);
    res.status(500).json({ error: 'Failed to fetch groups' });
  }
});

// POST /api/groups - accepts JSON group data and saves it
app.post('/api/groups', async (req, res) => {
  try {
    const groupData = req.body;
    
    // Validate required fields
    if (!groupData.name) {
      return res.status(400).json({ error: 'Group name is required' });
    }

    const newGroup = new Group(groupData);
    const savedGroup = await newGroup.save();
    
    res.status(201).json(savedGroup);
  } catch (error) {
    console.error('Error creating group:', error);
    res.status(500).json({ error: 'Failed to create group' });
  }
});

// Start server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
