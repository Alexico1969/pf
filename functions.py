import json
import os


def create_assistant(client):
    assistant_file_path = 'assistant.json'

    if os.path.exists(assistant_file_path):
        with open(assistant_file_path, 'r') as file:
            assistant_data = json.load(file)
            assistant_id = assistant_data['assistant_id']
            print("Loaded existing assistant ID.")
    else:
        file = client.files.create(file=open("dd_info.txt", "rb"),
                                   purpose='assistants')

        assistant = client.beta.assistants.create(
            instructions="""
                The assistant, Pathfinder Coach, helps previously incarcerated individuals find their way back into society. It is patient, understanding that it's a massive transition from life in prison to life outside of prison.
                """,
            model="gpt-4-1106-preview",
            tools=[{
                "type": "file_search"
            }]
        )

        with open(assistant_file_path, 'w') as file:
            json.dump({'assistant_id': assistant.id}, file)
            print("Created a new assistant and saved the ID.")

        assistant_id = assistant.id

    return assistant_id




'''
def create_assistant(client):
  assistant_file_path = 'assistant.json'

  if os.path.exists(assistant_file_path):
    with open(assistant_file_path, 'r') as file:
      assistant_data = json.load(file)
      assistant_id = assistant_data['assistant_id']
      print("Loaded existing assistant ID.")
  else:
    file = client.files.create(file=open("DreamDeferred-info.pdf", "rb"),
                               purpose='assistants')

    assistant = client.beta.assistants.create(instructions="""
          The assistant, Pathfinder Coach, helps previously incarcerated individuals find their way back into society. It is patient, understanding that it's a massive transition from life in prison to life outside of prison.
          """,
                                              model="gpt-4-1106-preview",
                                              tools=[{
                                                  "type": "retrieval"
                                              }],
                                              file_ids=[file.id])

    with open(assistant_file_path, 'w') as file:
      json.dump({'assistant_id': assistant.id}, file)
      print("Created a new assistant and saved the ID.")

    assistant_id = assistant.id

  return assistant_id
'''