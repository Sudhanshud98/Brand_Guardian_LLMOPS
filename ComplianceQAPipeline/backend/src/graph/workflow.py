'''
This module defines the DAG: Directed Acyclic Graph that orchestrates the video compliance audit process.
It connects the nodes using the StateGraph from LangGraph
START -> index_video_node-> audit_content_node -> END
'''

from langgraph.graph import StateGraph, START, END
from backend.src.graph.state import VideoAuditState
from backend.src.graph.nodes import (
    index_video_node,
    audit_content_node
)

def create_graph():
    '''
    Constructs and compiles the LangGraph workflow
    Returns:
    Compiled Graph: runnable graph object for execution
    '''
    # initialize the graph with state schema
    workflow = StateGraph (VideoAuditState)
    #add the nodes
    workflow.add_node("indexer", index_video_node)
    workflow.add_node("auditor", audit_content_node)
    # define the entry point
    workflow.set_entry_point("indexer")
    # define the edges
    workflow.add_edge("indexer", "auditor")
    workflow.add_edge("auditor", END)

    app = workflow.compile()
    return app

app = create_graph()