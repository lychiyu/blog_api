# coding: utf-8

"""
 Created by liuying on 2018/8/16.
"""
from rest_framework import permissions


class BlogPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        return False
