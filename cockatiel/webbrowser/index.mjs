import { WebBrowser } from "langchain/tools/webbrowser";
import { ChatOpenAI } from "langchain/chat_models/openai";
import { OpenAIEmbeddings } from "langchain/embeddings/openai";
export async function run() {
    const model = new ChatOpenAI({ temperature: 0 });
    
    const embeddings = new OpenAIEmbeddings(process.env.OPENAI_API_KEY
        ? { azureOpenAIApiDeploymentName: "Embeddings2" }
        : {});
    
        const browser = new WebBrowser({ model, embeddings });
    
        const result = await browser.call(`"https://weather.com/weather/tenday/l/26bdad6cf32cb6abe0d10d7d2bbfd50d5e6d9ba3cb32d61fdaafa585fd4465fe","What is the weather forecast for the next few days?"`);
    
        console.log(result);
}
run().catch(err => console.error(err));
