import React from 'react'
import Head from 'next/head'

const members = [
  {name: 'Dr. Alice Morgan', role: 'Director', email: 'alice@datascienceclub.edu'},
  {name: 'Samir Patel', role: 'Operations Chair', email: 'samir@datascienceclub.edu'},
  {name: 'Li Wei', role: 'Programs Lead', email: 'li@datascienceclub.edu'},
  {name: 'Jessica Park', role: 'Research Director', email: 'jessica@datascienceclub.edu'},
  {name: 'Michael Torres', role: 'Outreach Coordinator', email: 'michael@datascienceclub.edu'},
  {name: 'Priya Singh', role: 'Events Coordinator', email: 'priya@datascienceclub.edu'}
]

export default function Team(){
  return (
    <>
      <Head><title>Team — Data Science Club</title></Head>

      <h1 className="text-4xl font-bold mb-2" style={{color: 'var(--primary)'}}>Executive Team</h1>
      <p className="text-lg text-slate-700 mb-12 pb-4 border-b-2" style={{borderBottomColor: 'rgba(0, 61, 153, 0.2)'}}>Meet the leaders driving our mission forward</p>

      <div className="grid md:grid-cols-3 gap-6">
        {members.map((m, idx) => (
          <div key={m.name} className="border-l-4 p-6 bg-gradient-to-br from-blue-50 to-white rounded-lg hover:shadow-lg transition-all duration-300 group" style={{borderLeftColor: 'var(--accent)', boxShadow: '0 2px 8px rgba(10, 61, 98, 0.08)'}}>
            <div className="inline-flex items-center justify-center w-12 h-12 rounded-full mb-4 text-white font-bold" style={{backgroundColor: 'var(--accent)'}}>
              {m.name.split(' ').map(n => n[0]).join('').substring(0, 2)}
            </div>
            <div className="font-semibold text-lg mb-1 group-hover:translate-x-1 transition-transform duration-300" style={{color: 'var(--primary)'}}>{m.name}</div>
            <div className="text-sm font-medium mb-4 px-2 py-1 inline-block rounded" style={{backgroundColor: 'rgba(0, 61, 153, 0.1)', color: 'var(--accent)'}}>{m.role}</div>
            <div className="pt-4 border-t border-gray-200">
              <a href={`mailto:${m.email}`} className="text-sm text-slate-600 hover:font-medium transition-all duration-300" style={{color: 'text-slate-600'}}>
                {m.email}
              </a>
            </div>
          </div>
        ))}
      </div>
    </>
  )
}
