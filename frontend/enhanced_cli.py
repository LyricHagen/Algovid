#!/usr/bin/env python3
"""
Enhanced Python CLI for Algovid group management.
This provides the same functionality as the Swift CLI but with additional features.
"""

import urllib.request
import urllib.parse
import json
import sys
import os
from datetime import datetime

class EnhancedGroupCLI:
    def __init__(self):
        self.base_url = "http://localhost:4000/api"
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def make_request(self, url, method="GET", data=None):
        """Make HTTP request using urllib"""
        req = urllib.request.Request(url, method=method)
        
        if data:
            req.add_header('Content-Type', 'application/json')
            req.data = json.dumps(data).encode('utf-8')
        
        try:
            with urllib.request.urlopen(req) as response:
                return response.read().decode('utf-8')
        except urllib.error.URLError as e:
            raise Exception(f"Request failed: {e}")
    
    def test_connection(self):
        """Test if the backend is running"""
        try:
            self.make_request(f"{self.base_url}/groups")
            return True
        except:
            return False
    
    def list_groups(self):
        """Fetch and display all groups with enhanced formatting"""
        try:
            response_data = self.make_request(f"{self.base_url}/groups")
            groups = json.loads(response_data)
            
            if not groups:
                print("📭 No groups found in the database.")
                return
            
            print(f"\n📋 Found {len(groups)} group(s):")
            print("=" * 50)
            
            for i, group in enumerate(groups, 1):
                print(f"\n{i}. 🏷️  {group['name']}")
                print(f"   📝 Description: {group['description'] or 'No description'}")
                if group.get('_id'):
                    print(f"   🆔 ID: {group['_id']}")
                if group.get('structure'):
                    print(f"   🏗️  Structure: {json.dumps(group['structure'], indent=2)}")
                print("-" * 30)
                
        except Exception as e:
            print(f"❌ Error fetching groups: {e}")
    
    def add_group(self):
        """Add a new group with enhanced input validation"""
        print("\n" + "=" * 50)
        print("➕ ADD NEW GROUP")
        print("=" * 50)
        
        # Get group name
        while True:
            name = input("🏷️  Enter group name: ").strip()
            if name:
                break
            print("❌ Group name cannot be empty. Please try again.")
        
        # Get description
        description = input("📝 Enter group description (optional): ").strip()
        
        # Get structure
        print("\n🏗️  Group Structure (JSON format)")
        print("Examples:")
        print('  - Simple: {"type": "cyclic", "order": 3}')
        print('  - Complex: {"type": "multiplication_table", "table": {...}}')
        print('  - Empty: (press Enter to skip)')
        
        structure_input = input("\nEnter structure as JSON: ").strip()
        structure = {}
        
        if structure_input:
            try:
                structure = json.loads(structure_input)
                print("✅ JSON structure parsed successfully!")
            except json.JSONDecodeError as e:
                print(f"❌ Invalid JSON: {e}")
                print("Using empty structure instead.")
        
        # Confirm before creating
        print(f"\n📋 Summary:")
        print(f"   Name: {name}")
        print(f"   Description: {description or 'None'}")
        print(f"   Structure: {json.dumps(structure) if structure else 'Empty'}")
        
        confirm = input("\n🤔 Create this group? (y/N): ").strip().lower()
        if confirm not in ['y', 'yes']:
            print("❌ Group creation cancelled.")
            return
        
        # Create the group
        group_data = {
            "name": name,
            "description": description,
            "structure": structure
        }
        
        try:
            print("\n🔄 Creating group...")
            response_data = self.make_request(f"{self.base_url}/groups", 
                                           method="POST", 
                                           data=group_data)
            created_group = json.loads(response_data)
            
            print("✅ Group created successfully!")
            print("=" * 50)
            print(f"🏷️  Name: {created_group['name']}")
            print(f"📝 Description: {created_group['description']}")
            if created_group.get('_id'):
                print(f"🆔 ID: {created_group['_id']}")
            print("=" * 50)
                
        except Exception as e:
            print(f"❌ Error creating group: {e}")
    
    def delete_group(self):
        """Delete a group by ID"""
        print("\n🗑️  DELETE GROUP")
        print("=" * 50)
        
        # First list all groups
        try:
            response_data = self.make_request(f"{self.base_url}/groups")
            groups = json.loads(response_data)
            
            if not groups:
                print("📭 No groups to delete.")
                return
            
            print("Available groups:")
            for i, group in enumerate(groups, 1):
                print(f"{i}. {group['name']} (ID: {group.get('_id', 'N/A')})")
            
            try:
                choice = int(input("\nEnter the number of the group to delete: ")) - 1
                if 0 <= choice < len(groups):
                    group = groups[choice]
                    confirm = input(f"🗑️  Delete '{group['name']}'? (y/N): ").strip().lower()
                    if confirm in ['y', 'yes']:
                        # Note: We'd need to add a DELETE endpoint to the backend
                        print("⚠️  Delete functionality requires backend support.")
                        print("   (Backend currently only supports GET and POST)")
                else:
                    print("❌ Invalid choice.")
            except ValueError:
                print("❌ Please enter a valid number.")
                
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def show_stats(self):
        """Show database statistics"""
        try:
            response_data = self.make_request(f"{self.base_url}/groups")
            groups = json.loads(response_data)
            
            print("\n📊 DATABASE STATISTICS")
            print("=" * 50)
            print(f"📈 Total groups: {len(groups)}")
            
            if groups:
                # Analyze group names
                names = [g['name'] for g in groups]
                print(f"📝 Sample names: {', '.join(names[:3])}{'...' if len(names) > 3 else ''}")
                
                # Check for groups with structures
                with_structures = sum(1 for g in groups if g.get('structure'))
                print(f"🏗️  Groups with structures: {with_structures}")
            
            print("=" * 50)
            
        except Exception as e:
            print(f"❌ Error getting stats: {e}")

    def validate_group(self):
            """Validate a group's structure using group theory axioms"""
            print("\n🔍 VALIDATE GROUP")
            print("=" * 50)
            
            # First list all groups
            try:
                response_data = self.make_request(f"{self.base_url}/groups")
                groups = json.loads(response_data)
                
                if not groups:
                    print("📭 No groups to validate.")
                    return
                
                print("Available groups:")
                for i, group in enumerate(groups, 1):
                    print(f"{i}. {group['name']} (ID: {group.get('_id', 'N/A')})")
                
                try:
                    choice = int(input("\nEnter the number of the group to validate: ")) - 1
                    if 0 <= choice < len(groups):
                        group = groups[choice]
                        print(f"\n🔍 Validating group: {group['name']}")
                        print("=" * 50)
                        
                        # Check if group has a structure to validate
                        if not group.get('structure') or not group['structure'].get('table'):
                            print("⚠️  This group has no multiplication table to validate.")
                            print("   Only groups with 'table' structures can be validated.")
                            return
                        
                        # Import and use the validation function
                        try:
                            import sys
                            import os
                            # Add the math directory to the path
                            math_path = os.path.join(os.path.dirname(__file__), '..', 'math')
                            sys.path.insert(0, math_path)
                            
                            from group_utils import is_valid_group, find_identity, find_inverse, get_group_elements
                            
                            table = group['structure']['table']
                            elements = get_group_elements(table)
                            
                            print(f"🏷️  Group: {group['name']}")
                            print(f"📝 Description: {group['description'] or 'No description'}")
                            print(f"🔢 Elements: {', '.join(sorted(elements))}")
                            print(f"📊 Order: {len(elements)}")
                            print("-" * 30)
                            
                            # Validate the group
                            print("🔍 Checking group theory axioms...")
                            is_valid = is_valid_group(table)
                            
                            if is_valid:
                                print("✅ VALID GROUP! All axioms satisfied.")
                                print("\n📋 Axiom Check Results:")
                                print("   ✅ Closure: Every product is in the group")
                                print("   ✅ Associativity: (a * b) * c = a * (b * c)")
                                print("   ✅ Identity: Identity element exists")
                                print("   ✅ Inverses: Every element has an inverse")
                                
                                # Show additional properties
                                identity = find_identity(table)
                                if identity:
                                    print(f"\n🆔 Identity element: {identity}")
                                    
                                    # Show inverses
                                    print("\n🔄 Element inverses:")
                                    for element in sorted(elements):
                                        if element != identity:
                                            inverse = find_inverse(table, element)
                                            if inverse:
                                                print(f"   {element}⁻¹ = {inverse}")
                            else:
                                print("❌ NOT A VALID GROUP! Some axioms failed.")
                                print("\n📋 Axiom Check Results:")
                                print("   ❌ One or more group axioms are not satisfied")
                                print("   💡 Check your multiplication table structure")
                            
                        except ImportError as e:
                            print(f"❌ Error importing validation functions: {e}")
                            print("   Make sure the math/group_utils.py file is available")
                        except Exception as e:
                            print(f"❌ Error during validation: {e}")
                            
                    else:
                        print("❌ Invalid choice.")
                except ValueError:
                    print("❌ Please enter a valid number.")
                    
            except Exception as e:
                print(f"❌ Error: {e}")
    
    def run(self):
        """Main CLI loop with enhanced menu"""
        print("🚀 ENHANCED GROUP MANAGEMENT CLI")
        print("=" * 50)
        print("Built with Python (Swift CLI temporarily unavailable)")
        print("=" * 50)
        
        # Test connection
        if not self.test_connection():
            print("❌ Cannot connect to backend server!")
            print("   Make sure the backend is running on http://localhost:4000")
            return
        
        print("✅ Connected to backend server")
        
        while True:
            print("\n" + "=" * 50)
            print("📋 MAIN MENU")
            print("=" * 50)
            print("1. 📋 List all groups")
            print("2. ➕ Add new group")
            print("3. 🗑️  Delete group")
            print("4. 🔍 Validate group")
            print("5. 📊 Show statistics")
            print("6. 🔄 Test connection")
            print("7. 🚪 Exit")
            print("=" * 50)
            
            try:
                choice = input("Enter your choice (1-7): ").strip()
                
                if choice == "1":
                    self.list_groups()
                elif choice == "2":
                    self.add_group()
                elif choice == "3":
                    self.delete_group()
                elif choice == "4":
                    self.validate_group()
                elif choice == "5":
                    self.show_stats()
                elif choice == "6":
                    if self.test_connection():
                        print("✅ Backend connection is working!")
                    else:
                        print("❌ Backend connection failed!")
                elif choice == "7":
                    print("\n👋 Goodbye! Thanks for using Algovid!")
                    break
                else:
                    print("❌ Invalid choice. Please enter 1-7.")
                    
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except EOFError:
                print("\n👋 Goodbye!")
                break

def main():
    cli = EnhancedGroupCLI()
    cli.run()

if __name__ == "__main__":
    main() 