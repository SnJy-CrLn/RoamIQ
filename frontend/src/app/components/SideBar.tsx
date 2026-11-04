import RecentTrips from "./RecentTrips"
import SideBarHeader from "./SideBarHeader"
import SideBarNavSection from "./SideBarNavSection"
import Image from "next/image"

function SideBar() {
  return (
    <aside className='flex flex-col gap-4 bg-sidebar w-87.5 h-screen shrink-0 p-3.5'>
        <SideBarHeader />
        <SideBarNavSection />
        <hr className="my-6 border-t border-gray-500"/>
        <RecentTrips />
        <Image 
          src='/image.png'
          alt="sidebar-footer-img"
          height={250}
          width={320}
        />
    </aside>
  )
}

export default SideBar