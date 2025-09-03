"""
Group theory utilities for validating group multiplication tables.
"""

from typing import Dict, Any, Set


def is_valid_group(structure: dict) -> bool:
    """
    Validates if a multiplication table satisfies the basic group axioms.
    
    This function checks the four fundamental group axioms:
    1. Closure: Every product in the table is in the set of elements
    2. Associativity: (a * b) * c == a * (b * c) for all a, b, c
    3. Identity: There exists an element e where e * a == a * e == a for all a
    4. Inverses: For every element a, there exists b where a * b == b * a == e
    
    Args:
        structure: A dictionary representing the group's multiplication table.
                  Expected format: {element: {element: product}} where
                  structure[a][b] gives the product a * b.
    
    Returns:
        bool: True if all group axioms are satisfied, False otherwise.
    
    Example:
        >>> table = {
        ...     'e': {'e': 'e', 'a': 'a', 'b': 'b'},
        ...     'a': {'e': 'a', 'a': 'b', 'b': 'e'},
        ...     'b': {'e': 'b', 'a': 'e', 'b': 'a'}
        ... }
        >>> is_valid_group(table)
        True
    """
    
    # Get the set of elements from the structure
    elements = set(structure.keys())
    
    # Check if structure is well-formed (all elements have entries for all elements)
    for element in elements:
        if element not in structure or set(structure[element].keys()) != elements:
            return False
    
    # 1. Check Closure: every product must be in the set of elements
    for a in elements:
        for b in elements:
            product = structure[a][b]
            if product not in elements:
                return False
    
    # 2. Check Associativity: (a * b) * c == a * (b * c) for all a, b, c
    for a in elements:
        for b in elements:
            for c in elements:
                left_assoc = structure[structure[a][b]][c]
                right_assoc = structure[a][structure[b][c]]
                if left_assoc != right_assoc:
                    return False
    
    # 3. Check Identity: find element e where e * a == a * e == a for all a
    identity = None
    for candidate in elements:
        is_identity = True
        for element in elements:
            if (structure[candidate][element] != element or 
                structure[element][candidate] != element):
                is_identity = False
                break
        if is_identity:
            identity = candidate
            break
    
    if identity is None:
        return False
    
    # 4. Check Inverses: for every element a, there exists b where a * b == b * a == e
    for element in elements:
        has_inverse = False
        for candidate in elements:
            if (structure[element][candidate] == identity and 
                structure[candidate][element] == identity):
                has_inverse = True
                break
        if not has_inverse:
            return False
    
    return True


def get_group_elements(structure: dict) -> Set[str]:
    """
    Extract the set of group elements from a multiplication table.
    
    Args:
        structure: A dictionary representing the group's multiplication table.
    
    Returns:
        Set[str]: The set of group elements.
    """
    return set(structure.keys())


def find_identity(structure: dict) -> str:
    """
    Find the identity element in a group multiplication table.
    
    Args:
        structure: A dictionary representing the group's multiplication table.
    
    Returns:
        str: The identity element, or None if not found.
    """
    elements = set(structure.keys())
    
    for candidate in elements:
        is_identity = True
        for element in elements:
            if (structure[candidate][element] != element or 
                structure[element][candidate] != element):
                is_identity = False
                break
        if is_identity:
            return candidate
    
    return None


def find_inverse(structure: dict, element: str) -> str:
    """
    Find the inverse of an element in a group.
    
    Args:
        structure: A dictionary representing the group's multiplication table.
        element: The element to find the inverse of.
    
    Returns:
        str: The inverse element, or None if not found.
    """
    identity = find_identity(structure)
    if identity is None:
        return None
    
    elements = set(structure.keys())
    
    for candidate in elements:
        if (structure[element][candidate] == identity and 
            structure[candidate][element] == identity):
            return candidate
    
    return None 