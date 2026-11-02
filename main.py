from pydantic import BaseModel
from fastapi import FastAPI
from agent.agentic_workflow import Agent
from fastapi.responses import JSONResponse
import traceback
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

