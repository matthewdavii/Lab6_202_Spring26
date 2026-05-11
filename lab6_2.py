from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Node:
    val: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


def preorder(tree: Optional[Node]) -> list[int]:
    if tree is None:
        return []
    return [tree.val] + preorder(tree.left) + preorder(tree.right)


def inorder(tree: Optional[Node]) -> list[int]:
    if tree is None:
        return []
    return inorder(tree.left) + [tree.val] + inorder(tree.right)


def postorder(tree: Optional[Node]) -> list[int]:
    if tree is None:
        return []
    return postorder(tree.left) + postorder(tree.right) + [tree.val]


def bfs(tree: Optional[Node]) -> list[int]:
    if tree is None:
        return []
    q = [tree]
    l = []

    while len(q)>0:
        n = q.pop(0)
        l.append(n.val)
        if n.left != None:
            q.append(n.left)
        if n.right != None:
            q.append(n.right)
    return l

