# AI Engineer BBL — Multi-Agent RAG

โปรเจกต์ตัวอย่างระบบถาม–ตอบนโยบายบริษัทจากไฟล์ `knowledge_base.txt` โดยใช้ Agent หลายตัวร่วมกับ RAG เพื่อให้คำตอบอ้างอิงเฉพาะข้อมูลที่ค้นพบในฐานความรู้ และลดการตอบจากการคาดเดา

## เทคโนโลยีที่ใช้

- **OpenAI Agents SDK (`openai-agents`)** — สร้าง Agent, Tool และควบคุมลำดับการทำงาน
- **OpenAI Python SDK** — เชื่อมต่อ LLM ผ่าน API ที่รองรับ OpenAI Responses API
- **Sentence Transformers** — สร้าง embedding สำหรับ Semantic Search
- **โมเดล `sentence-transformers/all-MiniLM-L6-v2`** — แปลงคำถามและเนื้อหาเป็นเวกเตอร์
- **python-dotenv** — อ่านค่า API จากไฟล์ `.env`

## Agent ในระบบ

ระบบมี 2 Agent:

1. **Report Generator** รับคำถามจากผู้ใช้ เรียก Data Retriever และเรียบเรียงคำตอบให้สั้น ชัดเจน โดยใช้เฉพาะข้อมูลที่ค้นพบ
2. **Data Retriever** รับคำค้นจาก Report Generator แล้วเรียก `search_knowledge_base` เพื่อส่งข้อความดิบที่เกี่ยวข้องกลับไป โดยไม่ตอบคำถามเอง

ลำดับการทำงาน:

```text
ผู้ใช้ถามคำถาม
    ↓
Report Generator
    ↓ เรียก Agent ในรูปแบบ Tool
Data Retriever
    ↓ เรียก Function Tool
Semantic Search ใน knowledge_base.txt
    ↓ ส่ง 3 ข้อความที่ใกล้เคียงที่สุด
Report Generator เรียบเรียงคำตอบ
    ↓
แสดงผลให้ผู้ใช้
```

## RAG และ Semantic Search ทำงานอย่างไร

เมื่อเริ่มโปรแกรม ระบบจะแบ่ง `knowledge_base.txt` เป็นช่วงข้อความตามบรรทัดว่าง แล้วสร้าง embedding ของแต่ละช่วงไว้ในหน่วยความจำ จากนั้นเมื่อมีคำถาม ระบบจะ:

1. สร้าง embedding ของคำถามด้วย `all-MiniLM-L6-v2`
2. เปรียบเทียบความคล้ายคลึงกับ embedding ของทุกช่วงข้อความ
3. เลือก 3 ช่วงที่มีคะแนนสูงที่สุด (`top_k = 3`)
4. ส่งข้อความเหล่านั้นให้ Report Generator สร้างคำตอบ

โปรเจกต์นี้ยังไม่ใช้ Vector Database โดยคำนวณ Semantic Search จากข้อมูลในหน่วยความจำโดยตรง จึงเหมาะกับฐานความรู้ขนาดเล็ก

## การติดตั้ง

ต้องมี Python และอินเทอร์เน็ตสำหรับติดตั้งแพ็กเกจ รวมถึงดาวน์โหลดโมเดล embedding ในการรันครั้งแรก

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## การตั้งค่า API

สร้างไฟล์ `.env` จากตัวอย่าง:

```bash
cp .env.example .env
```

แก้ค่าใน `.env`:

```env
BBL_LLM_BASE_URL=https://your-api-endpoint
BBL_LLM_API_KEY=your-api-key
BBL_LLM_MODEL=your-model-name
```

- `BBL_LLM_BASE_URL` — Base URL ของบริการ LLM
- `BBL_LLM_API_KEY` — API Key สำหรับเรียกใช้งาน
- `BBL_LLM_MODEL` — ชื่อโมเดลที่ API รองรับ เช่น `gpt-5-mini`

ห้าม commit ไฟล์ `.env` หรือเผยแพร่ API Key โดยไฟล์นี้ถูกเพิ่มไว้ใน `.gitignore` แล้ว

## การรัน

รันคำสั่งจากโฟลเดอร์หลักของโปรเจกต์:

```bash
python -m src.main
```

จากนั้นพิมพ์คำถาม เช่น:

```text
Question: How many annual leave days do full-time employees receive?
```

ระหว่างทำงาน โปรแกรมจะแสดง log ของ Agent และ Tool ก่อนแสดงคำตอบสุดท้ายในส่วน `Answer:`

หากต้องการเพิ่มหรือแก้ไขความรู้ ให้แก้ไฟล์ `knowledge_base.txt` แล้วเริ่มโปรแกรมใหม่เพื่อสร้าง embedding ใหม่
