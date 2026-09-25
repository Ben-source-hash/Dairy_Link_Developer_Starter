import {useEffect,useState} from "react";
type Farmer={id:number;farmer_id:string;name:string;county:string;ward?:string;active:boolean};
const API="http://localhost:8000";
export default function App(){
 const [farmers,setFarmers]=useState<Farmer[]>([]); const [loading,setLoading]=useState(true);
 useEffect(()=>{fetch(`${API}/api/farmers`).then(r=>r.json()).then(setFarmers).finally(()=>setLoading(false));},[]);
 return <main className="app">
  <header className="topbar"><div><b className="brand">DAIRY LINK</b><div className="sub">Digital Dairy Value-Chain Platform</div></div><span className="tag">MVP</span></header>
  <section className="hero"><h1>Dairy Link Dashboard</h1><p>Farmers, animals, milk records and dairy services in one platform.</p></section>
  <section className="cards">{["Farmers","Animals","Milk Today","Payments"].map((x,i)=><div className="card" key={x}><span>{x}</span><strong>{i===0?farmers.length:"—"}</strong></div>)}</section>
  <section className="panel"><div className="head"><h2>Registered Farmers</h2><button onClick={()=>location.reload()}>Refresh</button></div>
  {loading?<p>Loading...</p>:farmers.length===0?<p>No farmers registered yet.</p>:<table><thead><tr><th>ID</th><th>Name</th><th>County</th><th>Ward</th><th>Status</th></tr></thead><tbody>{farmers.map(f=><tr key={f.id}><td>{f.farmer_id}</td><td>{f.name}</td><td>{f.county}</td><td>{f.ward??"—"}</td><td>{f.active?"Active":"Inactive"}</td></tr>)}</tbody></table>}</section>
 </main>;
}