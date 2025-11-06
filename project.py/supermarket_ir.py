import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

DB_FILE = "supermarket_ir.db"

def db_sakht():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS mohsoulat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            gheymat REAL NOT NULL,
            mojoodi INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def afzoodan_mohsoul(name, gheymat, mojoodi):
    try:
        conn = sqlite3.connect(DB_FILE)
        cur = conn.cursor()
        cur.execute("INSERT INTO mohsoulat (name, gheymat, mojoodi) VALUES (?, ?, ?)", (name, gheymat, mojoodi))
        conn.commit()
        conn.close()
        return True, "محصول اضافه شد"
    except sqlite3.IntegrityError:
        return False, "این محصول قبلاً ثبت شده است"
    except Exception as e:
        return False, f"خطا: {e}"

def list_mohsoulat():
    try:
        conn = sqlite3.connect(DB_FILE)
        cur = conn.cursor()
        cur.execute("SELECT id, name, gheymat, mojoodi FROM mohsoulat ORDER BY id")
        rows = cur.fetchall()
        conn.close()
        return rows
    except:
        return []

def update_mojoodi(pid, tedad):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("UPDATE mohsoulat SET mojoodi = mojoodi - ? WHERE id = ?", (tedad, pid))
    conn.commit()
    conn.close()

class SuperMarketApp:
    def __init__(self, root):
        self.root = root
        self.root.title("نرم‌افزار سوپرمارکت")
        self.root.geometry("920x560")
        self.sabad = []
        self.style = ttk.Style()
        try:
            self.style.theme_use('clam')
        except:
            pass

        upper = tk.LabelFrame(root, text="ثبت محصول جدید")
        upper.pack(fill="x", padx=12, pady=8)

        tk.Label(upper, text="نام محصول:").grid(row=0, column=0, padx=6, pady=6, sticky="w")
        self.name_entry = tk.Entry(upper)
        self.name_entry.grid(row=0, column=1, padx=6, pady=6)

        tk.Label(upper, text="قیمت (تومان):").grid(row=0, column=2, padx=6, pady=6, sticky="w")
        self.price_entry = tk.Entry(upper)
        self.price_entry.grid(row=0, column=3, padx=6, pady=6)

        tk.Label(upper, text="تعداد موجود:").grid(row=0, column=4, padx=6, pady=6, sticky="w")
        self.stock_entry = tk.Entry(upper)
        self.stock_entry.grid(row=0, column=5, padx=6, pady=6)

        tk.Button(upper, text="ثبت محصول", width=12, command=self.sabten_mohsoul).grid(row=0, column=6, padx=8, pady=6)

        mid = tk.LabelFrame(root, text="لیست محصولات")
        mid.pack(fill="both", expand=True, padx=12, pady=8)

        cols = ("id", "name", "gheymat", "mojoodi")
        self.table = ttk.Treeview(mid, columns=cols, show="headings", height=12)
        self.table.heading("id", text="شناسه")
        self.table.heading("name", text="نام محصول")
        self.table.heading("gheymat", text="قیمت (تومان)")
        self.table.heading("mojoodi", text="موجودی")
        self.table.column("id", width=70, anchor="center")
        self.table.column("name", width=380)
        self.table.column("gheymat", width=120, anchor="e")
        self.table.column("mojoodi", width=100, anchor="center")
        self.table.pack(fill="both", expand=True, side="left", padx=(6,0), pady=6)

        scrollbar = ttk.Scrollbar(mid, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="left", fill="y", padx=(0,6))

        right_panel = tk.Frame(root)
        right_panel.pack(fill="x", padx=12, pady=(0,12))

        sell_frame = tk.LabelFrame(right_panel, text="فروش و فاکتور")
        sell_frame.pack(fill="x", padx=0, pady=6)

        tk.Label(sell_frame, text="شناسه محصول:").grid(row=0, column=0, padx=6, pady=6, sticky="w")
        self.id_entry = tk.Entry(sell_frame, width=8)
        self.id_entry.grid(row=0, column=1, padx=6, pady=6)

        tk.Label(sell_frame, text="تعداد:").grid(row=0, column=2, padx=6, pady=6, sticky="w")
        self.count_entry = tk.Entry(sell_frame, width=8)
        self.count_entry.grid(row=0, column=3, padx=6, pady=6)

        tk.Button(sell_frame, text="افزودن به سبد", width=14, command=self.sabad_afzoodan).grid(row=0, column=4, padx=8)
        tk.Button(sell_frame, text="نمایش فاکتور", width=14, command=self.neshan_faktor).grid(row=0, column=5, padx=8)
        tk.Button(sell_frame, text="پاک کردن سبد", width=12, command=self.clear_sabad).grid(row=0, column=6, padx=8)

        cart_frame = tk.Frame(right_panel)
        cart_frame.pack(fill="both", padx=0, pady=6)

        cart_cols = ("name", "count", "unit", "total")
        self.cart_table = ttk.Treeview(cart_frame, columns=cart_cols, show="headings", height=6)
        self.cart_table.heading("name", text="نام محصول")
        self.cart_table.heading("count", text="تعداد")
        self.cart_table.heading("unit", text="قیمت واحد")
        self.cart_table.heading("total", text="جمع")
        self.cart_table.column("name", width=360)
        self.cart_table.column("count", width=80, anchor="center")
        self.cart_table.column("unit", width=120, anchor="e")
        self.cart_table.column("total", width=120, anchor="e")
        self.cart_table.pack(fill="both", expand=True, side="left", padx=(6,0))

        cart_scroll = ttk.Scrollbar(cart_frame, orient="vertical", command=self.cart_table.yview)
        self.cart_table.configure(yscroll=cart_scroll.set)
        cart_scroll.pack(side="left", fill="y", padx=(0,6))

        bottom_frame = tk.Frame(root)
        bottom_frame.pack(fill="x", padx=12, pady=(0,12))

        tk.Label(bottom_frame, text="جمع کل:").pack(side="left", padx=(6,0))
        self.total_var = tk.StringVar(value="0")
        tk.Label(bottom_frame, textvariable=self.total_var, font=("Tahoma", 11, "bold")).pack(side="left", padx=6)
        tk.Button(bottom_frame, text="بارگذاری محصولات", command=self.list_refresh).pack(side="right", padx=6)
        tk.Button(bottom_frame, text="حذف محصول انتخابی", command=self.delete_selected_product).pack(side="right", padx=6)

        self.list_refresh()

    def sabten_mohsoul(self):
        name = self.name_entry.get().strip()
        price = self.price_entry.get().strip()
        stock = self.stock_entry.get().strip()
        if not name or not price or not stock:
            messagebox.showwarning("هشدار", "لطفاً همه فیلدها را کامل کنید")
            return
        try:
            price_f = float(price)
            stock_i = int(stock)
            ok, msg = afzoodan_mohsoul(name, price_f, stock_i)
            if ok:
                self.name_entry.delete(0, "end")
                self.price_entry.delete(0, "end")
                self.stock_entry.delete(0, "end")
                self.list_refresh()
                messagebox.showinfo("پیغام", msg)
            else:
                messagebox.showerror("خطا", msg)
        except ValueError:
            messagebox.showerror("خطا", "قیمت باید عدد (مثلاً 12000) و موجودی باید عدد صحیح باشد")

    def list_refresh(self):
        for i in self.table.get_children():
            self.table.delete(i)
        rows = list_mohsoulat()
        for r in rows:
            self.table.insert("", "end", values=r)
        self.update_total_label()

    def sabad_afzoodan(self):
        try:
            pid = int(self.id_entry.get().strip())
            count = int(self.count_entry.get().strip())
        except:
            messagebox.showerror("خطا", "شناسه و تعداد باید عدد باشند")
            return
        rows = list_mohsoulat()
        found = None
        for r in rows:
            if r[0] == pid:
                found = r
                break
        if not found:
            messagebox.showwarning("یافت نشد", "محصولی با این شناسه پیدا نشد")
            return
        if found[3] < count:
            messagebox.showerror("موجودی کم", "موجودی کافی نیست")
            return
        unit = found[2]
        total = unit * count
        self.sabad.append({"id": pid, "name": found[1], "count": count, "unit": unit, "total": total})
        update_mojoodi(pid, count)
        self.cart_table.insert("", "end", values=(found[1], count, f"{unit:,.0f}", f"{total:,.0f}"))
        self.id_entry.delete(0, "end")
        self.count_entry.delete(0, "end")
        self.list_refresh()

    def update_total_label(self):
        total_all = sum(item["total"] for item in self.sabad)
        self.total_var.set(f"{total_all:,.0f} تومان")

    def neshan_faktor(self):
        if not self.sabad:
            messagebox.showwarning("خالی", "سبد خرید خالی است")
            return
        faktor_win = tk.Toplevel(self.root)
        faktor_win.title("فاکتور خرید")
        faktor_win.geometry("600x500")
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header = tk.Label(faktor_win, text="فاکتور فروش", font=("Tahoma", 14, "bold"))
        header.pack(pady=(10,4))
        tk.Label(faktor_win, text=f"تاریخ و زمان: {now}").pack()
        canvas = tk.Text(faktor_win, wrap="none")
        canvas.pack(fill="both", expand=True, padx=10, pady=10)
        canvas.tag_configure("right", justify="right")
        canvas.insert("end", "-"*60 + "\n")
        for idx, it in enumerate(self.sabad, start=1):
            line = f"{idx}. {it['name']} | تعداد: {it['count']} | قیمت واحد: {it['unit']:,.0f} | جمع: {it['total']:,.0f}\n"
            canvas.insert("end", line, "right")
        canvas.insert("end", "-"*60 + "\n")
        total_all = sum(item["total"] for item in self.sabad)
        canvas.insert("end", f"جمع کل: {total_all:,.0f} تومان\n\n", "right")
        canvas.insert("end", "با تشکر از خرید شما ❤️\n", "right")
        canvas.config(state="disabled")
        def close_and_clear():
            self.sabad.clear()
            for i in self.cart_table.get_children():
                self.cart_table.delete(i)
            self.list_refresh()
            faktor_win.destroy()
        tk.Button(faktor_win, text="تایید و بستن فاکتور", command=close_and_clear).pack(pady=(0,12))

    def clear_sabad(self):
        if not self.sabad:
            return
        if messagebox.askyesno("پاک کردن", "آیا از پاک کردن سبد خرید مطمئنید؟"):
            self.sabad.clear()
            for i in self.cart_table.get_children():
                self.cart_table.delete(i)
            self.list_refresh()

    def delete_selected_product(self):
        sel = self.table.selection()
        if not sel:
            messagebox.showwarning("هیچ‌چیز انتخاب نشده", "لطفاً یک محصول در لیست انتخاب کنید")
            return
        item = self.table.item(sel[0])
        pid = item["values"][0]
        if messagebox.askyesno("حذف", f"آیا می‌خواهید محصول با شناسه {pid} حذف شود؟"):
            try:
                conn = sqlite3.connect(DB_FILE)
                cur = conn.cursor()
                cur.execute("DELETE FROM mohsoulat WHERE id = ?", (pid,))
                conn.commit()
                conn.close()
                self.list_refresh()
            except Exception as e:
                messagebox.showerror("خطا", f"حذف انجام نشد: {e}")

if __name__ == "__main__":
    db_sakht()
    root = tk.Tk()
    app = SuperMarketApp(root)
    root.mainloop()
