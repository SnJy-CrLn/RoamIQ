from pydantic import BaseModel
from fastapi import FastAPI
from agent.agentic_workflow import Agent
from fastapi.responses import JSONResponse, FileResponse
import traceback
import os
from utils.save_as_doc import save_document
from starlette.background import BackgroundTask

app = FastAPI() 

class QueryRequest(BaseModel):
    query: str

@app.post('/query')
async def query_travel_agent(query:QueryRequest):
    try:
        print(query)
        graph = Agent()
        react_app = graph()
        messages = {"messages":[query.query]}
        output = react_app.invoke(messages)

        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content
        else:
            final_output = str(output)
        return {"answer": final_output}
    except Exception as e:
        print("\n========== ROAMIQ ERROR ==========")
        traceback.print_exc()
        print("==================================\n")
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post('/save-as-doc')
async def save_travel_doc(request:str):
    try:
        file_path = save_document(request.response)
        if not file_path:
            raise Exception("Document generation failed")

        return FileResponse(
            path = file_path,
            filename = 'RoamIQ travel plan.md',
            media_type = 'text/markdown',
            background = BackgroundTask(os.remove, file_path)
        )
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(
            status_code = 500,
            content= {'error': str(e)}
        )


