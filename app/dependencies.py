from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel
from uuid import UUID, uuid4
from enum import Enum